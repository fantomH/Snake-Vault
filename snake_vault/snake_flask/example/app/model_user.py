# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/model_user.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-20 12:31:46 UTC
# updated       : 2026-05-20 12:31:46 UTC
# description   : description

from dataclasses import dataclass
from werkzeug.security import generate_password_hash
import sqlite3

from flask import current_app

from .db import get_db


@dataclass
class User:
    username: str
    firstname: str
    lastname: str
    password_hash: str

    id: int | None = None
    email: str | None = None
    is_active: bool = False

    TABLE_NAME = "users"

    # [+] ------------------------------| create_table
    @classmethod
    def create_table(cls):

        conn = get_db(current_app.config["DATABASE"])

        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                email TEXT UNIQUE,
                password_hash TEXT NOT NULL,
                is_active INTEGER NOT NULL DEFAULT 0
            )
        """)

        conn.commit()

    # [+] ------------------------------| CREATE_USER 
    @classmethod
    def create_user(
        cls,
        username,
        firstname,
        lastname,
        password,
        email=None,
        is_active=False):

        password_hash = generate_password_hash(password)

        conn = get_db(current_app.config["DATABASE"])

        conn.execute(f"""
            INSERT INTO {cls.TABLE_NAME} (
                username,
                firstname,
                lastname,
                email,
                password_hash,
                is_active
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            username,
            firstname,
            lastname,
            email,
            password_hash,
            int(is_active)
        ))

        conn.commit()

    # ------------------------------| FETCH_BY_USERNAME
    @classmethod
    def fetch_by_username(cls, username):

        conn = get_db(current_app.config["DATABASE"])

        user = conn.execute(f"""
            SELECT *
            FROM {cls.TABLE_NAME}
            WHERE username = ?
        """, (
            username,
        )).fetchone()

        if user is None:
            return None

        return cls(**dict(user))

    # ------------------------------| FETCH_BY_ID
    @classmethod
    def fetch_by_id(cls, id):

        conn = get_db(current_app.config["DATABASE"])

        user = conn.execute(f"""
            SELECT *
            FROM {cls.TABLE_NAME}
            WHERE id = ?
        """, (
            id,
        )).fetchone()

        if user is None:
            return None

        return cls(**dict(user))

    # ------------------------------| fetch_by_email
    @classmethod
    def fetch_by_email(cls, email):

        conn = get_db(current_app.config["DATABASE"])

        user = conn.execute(f"""
            SELECT *
            FROM {cls.TABLE_NAME}
            WHERE email = ?
        """, (
            email,
        )).fetchone()

        if user is None:
            return None

        return cls(**dict(user))
