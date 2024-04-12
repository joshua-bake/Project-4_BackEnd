from app import db
from models.user import UserModel
from models.base import BaseModel


class MedicalTermModel(db.Model, BaseModel):
    __tablename__ = "medical_terms"

    id = db.Column(db.Integer, primary_key=True)

    term = db.Column(db.Text, nullable=False, unique=True)
    definition = db.Column(db.Text, nullable=False, unique=False)
    anatomy = db.Column(db.Text, nullable=False, unique=False)

    # ? Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # ? Relationships
    user = db.relationship("UserModel", backref="medical_terms")
