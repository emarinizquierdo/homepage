
# Python standard libraries
import os

# Third-party libraries
from flask import Flask
from flask_login import (
    LoginManager
)

from google.cloud import ndb

# App module imports
from core.model.user import User

client = ndb.Client()


def ndb_wsgi_middleware(wsgi_app):
    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware


app = Flask(__name__)
app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)  # Wrap the app in middleware.
app.secret_key = os.getenv("SECRET_KEY") or os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.id_attribute


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


from core import views
