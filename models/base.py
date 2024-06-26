from datetime import datetime, timezone
from app import db


class BaseModel:

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    def save(self):
        db.session.add(self)
        db.session.commit()

    # ! Added little method to call SQLAlchemy commands to delete my model.
    def remove(self):
        db.session.delete(self)
        db.session.commit()
