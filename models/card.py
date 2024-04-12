from app import db
from models.user import UserModel


class CardModel(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)

    question = db.Column(db.Text, nullable=False, unique=False)
    answer = db.Column(db.Text, nullable=False, unique=False)
    deck_id = db.Column(db.Integer, db.ForeignKey("decks.id"), nullable=False)

    deck = db.relationship("DeckModel", back_populates="deck")


# ? Check Nick's video on relationship.
# ? May need to change Card Model to Language model with its unique fields.
# ? Do we need a model for each Type of Flashcard Deck e.g. Language and Medical
# ? Or can we use Card Model as a template for all other deck flashcards.
