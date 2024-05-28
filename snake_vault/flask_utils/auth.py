# :----------------------------------------------------------------------- INFO
# :[snake_vault/flask_utils/auth.py]
# /author        : fantomH
# /created       : 2024-05-27 20:00:42 UTC
# /updated       : 2024-05-27 20:00:42 UTC
# /description   : Authentication utils.

# :-----/ (decorator) @login_required /-----:
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_app.config.get('DSV_IS_STANDALONE') == True:
            return f(*args, **kwargs)
        elif current_user.is_authenticated == True:
            return f(*args, **kwargs)
        else:
            flash(f"Accès interdit! Connectez-vous d'abord", category="error")
            session['next_url'] = request.url
            return redirect(url_for('auth.login'))

    return wrap
