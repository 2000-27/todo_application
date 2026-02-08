from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
import os
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()

def db_config(app):
    database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
    secret_key = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = secret_key
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)
    bcrypt.init_app(app)
