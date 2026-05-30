# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/routes/admin.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 16:01:48 UTC
# updated       : 2026-05-19 16:01:48 UTC
# description   : Admin routes.

from flask import (
    Blueprint,
    current_app,
    jsonify,
    render_template,
    request,
)

from ..linguae import ( get_display_language )
from ..login_manager import ( login_required )
from ..model_user import ( User )
from ..plugins.snake_flask_table import TableGenerator
from ..tables.admin import get_users_table

admin = Blueprint("admin", __name__)

# [+] ------------------------------| /admin/users
@admin.route("/admin/users/", methods=["GET", "POST"])
@login_required
def users():

    display_language = get_display_language()
    table_generator = get_users_table()

    if request.method == "POST":
        print(request)

    return render_template(
        "admin/users.html",
        table_generator=table_generator,
        display_language=display_language,
    )


# [+] ------------------------------| /admin/users/data/
@admin.route("/admin/users/data/")
@login_required
def users_data():

    table_generator = get_users_table()

    return jsonify(
        table_generator.get_data()
    )

# [+] ---------------| /admin/users/update/
@admin.route("/admin/users/update/", methods=["POST"])
@login_required
def users_update():


    data = request.get_json()

    User.update_user(
        data.get("id"),
        **{
            data.get("column"): data.get("value")
        }
    )

    return jsonify({
        "ok": True,
    })

# [+] ------------------------------| /admin/users/<username>/
@admin.route("/admin/users/account/<username>/", methods=["GET", "POST"])
def user_account(username):

    user_account = User.fetch_by_username(username)
    display_language = get_display_language()

    if request.method == "POST":

        form_data = {}

        form_data["firstname"] = request.form.get("firstname", "").strip()
        form_data["lastname"] = request.form.get("lastname", "").strip()
        form_data["email"] = request.form.get("email", "").strip()

        password1 = request.form.get("password1", "").strip()
        password2 = request.form.get("password2", "").strip()


        # validated = True

        # if len(form_data["firstname"]) < 1:
            # flash(display_language.get("USER-ACCOUNT-firstname", "First name") + " " + display_language.get("USER-ACCOUNT-cannot_be_empty", "cannot be empty"), "danger")
            # validated = False

        # if len(form_data["lastname"]) < 1:
            # flash(display_language.get("USER-ACCOUNT-lastname", "Last name") + " " + display_language.get("USER-ACCOUNT-cannot_be_empty", "cannot be empty"), "danger")
            # validated = False

        # if len(form_data["username"]) < 1:
            # flash(display_language["SIGNUP-user"] + " " + display_language["SIGNUP-cannot_be_empty"], "danger")
            # validated = False

        # if User.fetch_by_username(form_data["username"]):
            # flash(display_language["SIGNUP-user_already_exists"], "danger")
            # validated = False

        # if User.fetch_by_email(form_data["email"]):
            # flash(display_language["SIGNUP-email_already_exists"], "danger")
            # validated = False

        # if not is_valid_password(password1):
            # flash(display_language["SIGNUP-invalid_password"], "danger")
            # validated = False
            
        # if password1 != password2:
            # flash(display_language["SIGNUP-passwords_dont_match"], "danger")
            # validated = False

        # if not validated:
            # return render_template(
                # "auth/sign-up.html",
                # display_language=display_language,
                # form_data=form_data,
            # )

    return render_template(
        "admin/user-account.html",
        user_account=user_account,
        display_language=display_language,
    )
