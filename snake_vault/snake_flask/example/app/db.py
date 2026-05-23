# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/app/db.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 11:56:16 UTC
# updated       : 2026-05-20 19:17:18 UTC
# description   : Database.

from pathlib import Path
import shutil
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db(database):

    if "databases" not in g:
        g.databases = {}

    if database not in g.databases:

        conn = sqlite3.connect(database)

        conn.row_factory = sqlite3.Row

        g.databases[database] = conn

    return g.databases[database]


def close_db(error=None):

    databases = g.pop("databases", {})

    for conn in databases.values():
        conn.close()

@click.command("init-db")
@with_appcontext
def init_db():
    """
    Run in terminal `flask --app run init-db` to initialize the db.
    """

    from .model_user import User

    User.create_table()
    User.create_user(
        username="admin",
        firstname="",
        lastname="",
        email="not@email.com",
        password="password"
    )

    create_migration_table(current_app.config["DATABASE"])

    click.echo(
        "DATABASE db initialized. "
        "Default login: admin / password"
    )

# [+] ------------------------------| migration

# [+] create migration table
def create_migration_table(database):

    conn = get_db(database)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS schema_migrations (
            version TEXT PRIMARY KEY,
            applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

# [+] migrate
@click.command("migrate")
@click.option("--database", required=True)
@click.argument("migration_file")
@with_appcontext
def migrate_command(database, migration_file):

    db_path = Path(database)

    migration_path = (
        Path(current_app.root_path)
        .parent
        / "migrations"
        / migration_file
    )

    if not migration_path.exists():
        raise click.ClickException(
            f"Migration file not found: {migration_path}"
        )

    version = migration_path.name

    conn = get_db(database)

    row = conn.execute("""
        SELECT 1
        FROM schema_migrations
        WHERE version = ?
    """, (version,)).fetchone()

    if row:
        raise click.ClickException(
            f"Migration already applied: {version}"
        )

    backup_path = db_path.with_suffix(
        db_path.suffix + f".backup-{version}"
    )

    shutil.copy2(db_path, backup_path)

    click.echo(f"Backup created: {backup_path}")

    sql = migration_path.read_text()

    try:

        conn.execute("BEGIN")

        conn.executescript(sql)

        conn.execute("""
            INSERT INTO schema_migrations (version)
            VALUES (?)
        """, (version,))

        conn.commit()

    except Exception as e:

        conn.rollback()

        raise click.ClickException(
            f"Migration failed: {e}"
        )

    click.echo(f"Migration applied: {version}")
