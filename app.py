from flask import Flask
from view import task_bp, user_bp
from config import db_config
from models import UserModel ,TaskModel

app = Flask(__name__)
db_config(app)

app.register_blueprint(task_bp)
app.register_blueprint(user_bp)
