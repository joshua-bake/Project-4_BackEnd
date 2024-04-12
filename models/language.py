from app import db
from models.user import UserModel
from models.base import BaseModel


class LanguageModel(db.Model, BaseModel):
    __tablename__ = "languages"

    id = db.Column(db.Integer, primary_key=True)

    word = db.Column(db.Text, nullable=False, unique=True)
    translation = db.Column(db.Text, nullable=False, unique=False)
    example_of_sentence = db.Column(db.Text, nullable=False, unique=False)
    part_of_speech = db.Column(db.Text, nullable=False, unique=False)
    pronunciation = db.Column(db.Text, nullable=False, unique=False)

    # ? Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # ? Relationships
    user = db.relationship("UserModel", backref="languages")
