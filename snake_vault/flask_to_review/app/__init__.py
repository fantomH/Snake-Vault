# :----------------------------------------------------------------------- INFO
# [Snake-Vault/snake_vault/flask/app/__init__.py]
# /author        : fantomH 
# /created       : 2024-03-21 01:43:40 UTC
# /updated       : 2024-03-21 01:43:40 UTC
# /description   : Basic flask app factory.

from flask import (Flask)

# :----- [INIT MODULES]
# db = SQLAlchemy()

# :----- [APPLICATION]

def create_app():

    # :If using a config file (../instance/config.py):
    # app = Flask(__name__, instance_relative_config=True)
    # app.config.from_pyfile("config.py")
    # :Else:
    app = Flask(__name__)

    # :Basic route.
    @app.route("/")
    def home():
        return "<h1>You landed here!</h1>"

    # :Initialize blueprints and handlers.

    # :(AUTH)
    # from routes.auth import auth
    # app.register_blueprint(auth, url_prefix="/")

    # :(HTTP status codes)
    """
    # :The error handlers for HTTP status codes are in .routes
    # :In order to work app-wide you must import them here.
    # :ref. https://flask.palletsprojects.com/en/2.2.x/errorhandling/
    """
    from .routes import not_found
    app.register_error_handler(404, not_found)

    # :----- (DATABASE)
    # :Import models
    # from .models import (User)

    # :DB initialization/creation.    
    # db.init_app(app)
    # with app.app_context():
        # if not os.path.exists("instance/" + app.config["DB_NAME"]):
            # db.create_all()
            # print("Created database!")

    # migrate.init_app(app, db)

    # :----- (LOGIN)
    # login_manager.login_view = "auth.login"
    # login_manager.refresh_view = "auth.login"
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
        # return User.query.get(int(id))

    # :----- (SESSION)
    # @app.before_request
    # def session_timeout():
        """
        ref. https://www.bonser.dev/blog/basic-flask-session-timeout-on-inactivity
        This technique is not satisfactory right now:
        1 / Needs a new request to logout, otherwise stays on a page.
        2 / If on a page for more than the permanent_session_lifetime, no
            request are sent, thus on the next one you will be logged out.
        """
        # session.permanent = True
        # app.permanent_session_lifetime = datetime.timedelta(minutes=app.config['SESSION_TIMEOUT'])
        # session.modified = True
        # g.user = current_user

    return app

# :------------------------------------------------------------- FIN ¯\_(ツ)_/¯
