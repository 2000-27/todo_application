from config import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.now(),
        nullable=False
    )

    # relationship → one user has many tasks
    tasks = db.relationship(
        "TaskModel",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, user_password):
        return check_password_hash(self.password, user_password)
    
    def __repr__(self):
        return f'<{self.email}>'