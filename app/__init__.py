from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import get_database_uri_value

app = Flask('contato_app')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri_value()
db = SQLAlchemy(app)

from app.utils.create_db import init_db
#init_db()

from .routes.user_route import bp_users
from .routes.contact_route import bp_contact
from .routes.auth_route import bp_auth

app.register_blueprint(bp_users, url_prefix='/users')
app.register_blueprint(bp_contact, url_prefix='/users/contact')
app.register_blueprint(bp_auth, url_prefix='/auth')
