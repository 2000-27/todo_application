from config import db
from datetime import datetime
import enum

class Status(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    START = "start"


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    heading = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    is_complete = db.Column(db.Boolean, default=False, nullable=False)

    status = db.Column(
        db.Enum(Status),
        default=Status.PENDING,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    def __repr__(self):
        return f"<Task {self.id} - {self.heading}- {self.description} ({self.status.value})>"
