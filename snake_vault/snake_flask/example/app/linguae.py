# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/linguae.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 20:29:22 UTC
# updated       : 2026-05-19 20:29:22 UTC
# description   : Language functions.

from flask import (
    current_app,
    url_for
)
from markupsafe import (
    Markup,
)

english = {
    "BUTTON-save": "Save",
    "HOME-title": "Welcome",
    "HOME-h1": "Welcome",
    "LOGIN-title": "Log In",
    "LOGIN-h1": "Log In",
    "LOGIN-user": "User",
    "LOGIN-user_placeholder": "Enter your username",
    "LOGIN-password": "Password",
    "LOGIN-password_placeholder": "Enter your password",
    "LOGIN-login": "Log In",
    "LOGIN-wrong_password": "Username or password is incorrect.",
    "LOGIN-account_not_active": "Your account must be activated. Contact your administrator.",
    "LOGIN-please_sign_up": Markup(
        f'This account does not exist. '
        f'Please sign up '
        f'<a href="../sign-up/">here</a>'),
    "MYACCOUNT-title": "My Account",
    "MYACCOUNT-h1": "My Account ",
    "MYACCOUNT-firstname_label": "First Name",
    "MYACCOUNT-lastname_label": "Last Name",
    "MYACCOUNT-email_label": "Email",
    "MYACCOUNT-change_your_password": "Change your password",
    "MYACCOUNT-current_password_label": "Current password",
    "MYACCOUNT-current_password_placeholder": "Enter you current password",
    "MYACCOUNT-new_password_label": "New password",
    "MYACCOUNT-new_password_placeholder": "Enter your new password",
    "MYACCOUNT-confirm_password_label": "Confirmation of new password",
    "MYACCOUNT-confirm_password_placeholder": "Confirm your new password",
    "SIGNUP-title": "Sign Up",
    "SIGNUP-h1": "Sign Up",
    "SIGNUP-message": Markup("Message<br/>Message"),
    "SIGNUP-cannot_be_empty": "cannot be empty!",
    "SIGNUP-firstname": "First Name",
    "SIGNUP-firstname_placeholder": "Enter your first name",
    "SIGNUP-lastname": "Last Name",
    "SIGNUP-lastname_placeholder": "Enter your last name",
    "SIGNUP-user": "Username",
    "SIGNUP-user_already_exists": "User already exists!",
    "SIGNUP-user_placeholder": "Choose a username",
    "SIGNUP-email": "Email",
    "SIGNUP-email_already_exists": "Email already exists!",
    "SIGNUP-email_placeholder": "Enter your email",
    "SIGNUP-password1": "Password",
    "SIGNUP-password1_placeholder": "Choose a password",
    "SIGNUP-invalid_password": Markup(
                               """
                               <strong>Password requirements:</strong>
                               <ul class="mb-0">
                                   <li>At least 8 characters</li>
                                   <li>One lowercase letter</li>
                                   <li>One uppercase letter</li>
                                   <li>One number</li>
                                   <li>One special character</li>
                               </ul>
                               """
                               ),
    "SIGNUP-password2": "Password Confirmation",
    "SIGNUP-password2_placeholder": "Confirm your password",
    "SIGNUP-submit_button": "Submit",
    "SIGNUP-passwords_dont_match": "Passwords don't match!",
}

french = {
    "HOME-title": "Bienvenu",
    "HOME-h1": "Bienvenu",
    "LOGIN-title": "Connexion",
    "LOGIN-h1": "Connexion",
    "LOGIN-user": "Utilisateur",
    "LOGIN-user_placeholder": "Entrez votre nom d'utilisateur",
    "LOGIN-password": "Mot de passe",
    "LOGIN-password_placeholder": "Entrez votre mot de passe",
    "LOGIN-login": "Connexion",
    "LOGIN-wrong_password": "Le nom d'utilisateur ou le mot de passe est incorrect.",
    "SIGNUP-title": "Inscription",
    "SIGNUP-h1": "Inscription",
    "SIGNUP-message": Markup("Message<br/>Message"),
    "SIGNUP-cannot_be_empty": "ne peut être vide!",
    "SIGNUP-firstname": "Prénom",
    "SIGNUP-firstname_placeholder": "Entrer votre prénom",
    "SIGNUP-lastname": "Nom",
    "SIGNUP-lastname_placeholder": "Entrer votre nom de famille",
    "SIGNUP-user": "Utilisateur",
    "SIGNUP-user_already_exists": "L'utilisateur existe déjà!",
    "SIGNUP-user_placeholder": "Choisir un nom d'utilisateur",
    "SIGNUP-email": "Courriel",
    "SIGNUP-email_already_exists": "Ce courriel est déjà utilisé!",
    "SIGNUP-email_placeholder": "Entrer votre courriel",
    "SIGNUP-password1": "Mot de passe",
    "SIGNUP-password1_placeholder": "Choisir un mot de passe",
    "SIGNUP-invalid_password": Markup(
                                      """
                                      <strong>Exigences du mot de passe&nbsp;:</strong>
                                      <ul class="mb-0">
                                          <li>Au moins 8 caractères</li>
                                          <li>Une lettre minuscule</li>
                                          <li>Une lettre majuscule</li>
                                          <li>Un chiffre</li>
                                          <li>Un caractère spécial</li>
                                      </ul>
                                      """
                               ),
    "SIGNUP-password2": "Confirmation du mot de passe",
    "SIGNUP-password2_placeholder": "Confirmer votre mot de passe",
    "SIGNUP-submit_button": "Soumettre",
    "SIGNUP-passwords_dont_match": "Les mots de passe ne concordent pas!",
}

languages = {
    "english": english,
    "french": french
}

def get_display_language():

    return languages[current_app.config["DISPLAY_LANGUAGE"]]
