
# Python standard libraries
import os
from datetime import timedelta

# Third-party libraries
from flask import Flask, session
from flask_login import (
    LoginManager
)

from google.cloud import ndb

# App module imports
from core.model.user import User
from core.properties import Properties

client = ndb.Client()
properties = Properties()

def ndb_wsgi_middleware(wsgi_app):
    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware


app = Flask(__name__)
app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)  # Wrap the app in middleware.
app.secret_key = properties.get("SECRET_KEY", os.urandom(24))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.id_attribute


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

from core import views
