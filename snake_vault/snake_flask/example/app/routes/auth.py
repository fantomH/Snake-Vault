# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/routes/auth.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 16:01:48 UTC
# updated       : 2026-05-19 16:01:48 UTC
# description   : Authentication routes.

from flask import (
    Blueprint,
    current_app,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from werkzeug.security import (
    check_password_hash
)

from ..linguae import (
    get_display_language
)
from ..login_manager import (
    login_required
)
from ..model_user import (
    User
)
from ..validator import (
    is_valid_password
)

auth = Blueprint("auth", __name__)

# [+] ------------------------------| login
@auth.route('/login/', methods=['GET', 'POST'])
def login():

    display_language = get_display_language()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.fetch_by_username(username)

        if user:
            if user.is_active:
                if check_password_hash(user.password_hash, password):

                    session.clear()
                    session["user_id"] = user.id
                    session.permanent = True

                    next_page = request.args.get("next")

                    if (
                        not next_page
                        or not next_page.startswith("/")
                        or next_page.startswith("/logout")
                    ):
                        next_page = url_for("index")

                    return redirect(next_page)
                else:
                    flash(display_language["LOGIN-wrong_password"], "danger")
            else:
                flash(display_language["LOGIN-account_not_active"], "danger")
        else:
            flash(display_language["LOGIN-please_sign_up"], "danger")
        

    return render_template(
        'auth/login.html',
        title=display_language["LOGIN-title"],
        display_language=display_language
    )

# [+] ------------------------------| sign-up
@auth.route("/sign-up/", methods=["GET", "POST"])
def sign_up():

    display_language = get_display_language()

    form_data = {
        "firstname": "",
        "lastname": "",
        "username": "",
        "email": "",
    }

    if request.method == "POST":
        form_data["firstname"] = request.form.get("firstname", "").strip()
        form_data["lastname"] = request.form.get("lastname", "").strip()
        form_data["username"] = request.form.get("username", "").strip()
        form_data["email"] = request.form.get("email", "").strip()

        password1 = request.form.get("password1").strip()
        password2 = request.form.get("password2").strip()

        validated = True

        if len(form_data["firstname"]) < 1:
            flash(display_language["SIGNUP-firstname"] + " " + display_language["SIGNUP-cannot_be_empty"], "danger")
            validated = False

        if len(form_data["lastname"]) < 1:
            flash(display_language["SIGNUP-lastname"] + " " + display_language["SIGNUP-cannot_be_empty"], "danger")
            validated = False

        if len(form_data["username"]) < 1:
            flash(display_language["SIGNUP-user"] + " " + display_language["SIGNUP-cannot_be_empty"], "danger")
            validated = False

        if User.fetch_by_username(form_data["username"]):
            flash(display_language["SIGNUP-user_already_exists"], "danger")
            validated = False

        if User.fetch_by_email(form_data["email"]):
            flash(display_language["SIGNUP-email_already_exists"], "danger")
            validated = False

        if not is_valid_password(password1):
            flash(display_language["SIGNUP-invalid_password"], "danger")
            validated = False
            
        if password1 != password2:
            flash(display_language["SIGNUP-passwords_dont_match"], "danger")
            validated = False

        if not validated:
            return render_template(
                "auth/sign-up.html",
                display_language=display_language,
                form_data=form_data,
            )

        # [+] Create user
        User.create_user(
            username=form_data["username"],
            firstname=form_data["firstname"],
            lastname=form_data["lastname"],
            email=form_data["email"],
            password=password1,
        )
        flash("Account created.", "success")
        return redirect(url_for("auth.login"))

    return render_template(
        "auth/sign-up.html",
        display_language=display_language,
        form_data=form_data,
    )

# [+] ------------------------------| my-account
@auth.route("/my-account/", methods=["GET", "POST"])
def my_account():

    display_language = get_display_language()

    return render_template(
        'auth/my-account.html',
        display_language=display_language,
    )

# [+] ------------------------------| logout
@auth.route("/logout/", methods=['GET', 'POST'])
@login_required
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
