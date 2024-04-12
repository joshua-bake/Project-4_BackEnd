from app import app, db
from models.user import UserModel
from models.deck import DeckModel
from models.card import CardModel
from models.collaborator import CollaboratorModel

with app.app_context():

    try:
        print("Creating our database...")
        db.drop_all()
        db.create_all()

        print("Seeding the database!")

    except Exception as e:
        print(e)
