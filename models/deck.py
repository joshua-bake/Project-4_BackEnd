from app import db
from models.user import UserModel


class DeckModel(db.Model):
    __tablename__ = "decks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("creators_id"), nullable=False)

    cards = db.relationship("CardModel", back_populates="deck")
    collaborators = db.relationship("CollboratorModel", back_populates="deck")
    user = db.relationship("UserModel", back_populates="deck")
