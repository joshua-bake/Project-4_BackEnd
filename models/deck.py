from app import db
from models.user import UserModel
from models.base import BaseModel


class DeckModel(db.Model, BaseModel):
    __tablename__ = "decks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=False)

    # ? Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # ? Relationships
    card = db.relationship("CardModel", back_populates="deck")
    user = db.relationship("UserModel", backref="decks")
