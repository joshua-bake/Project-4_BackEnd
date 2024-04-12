from app import db
from models.user import UserModel


class CollaboratorModel(db.Model):
    __tablename__ = "collaborators"

    id = db.Column(db.Integer, primary_key=True)

    deck_id = db.Column(db.Integer, db.ForeignKey("decks.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
