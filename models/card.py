from app import db
from models.base import BaseModel


class CardModel(db.Model, BaseModel):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)

    question = db.Column(db.Text, nullable=False, unique=False)
    answer = db.Column(db.Text, nullable=False, unique=False)

    # ? Foreign Keys
    deck_id = db.Column(db.Integer, db.ForeignKey("decks.id"), nullable=False)

    # ? Relationships
