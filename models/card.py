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


# ? Check Nick's video on relationship.
# ? May need to change Card Model to Language model with its unique fields.
# ? Do we need a model for each Type of Flashcard Deck e.g. Language and Medical
# ? Or can we use Card Model as a template for all other deck flashcards.
