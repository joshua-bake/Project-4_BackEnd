from app import app, db
from models.user import UserModel
from models.deck import DeckModel
from models.card import CardModel
from models.language import LanguageModel
from models.medical_term import MedicalTermModel

with app.app_context():

    try:
        print("Creating our database! 🫧")
        db.drop_all()
        db.create_all()

        josh = UserModel(
            username="josh", email="josh@josh.com", password="adminpassword"
        )
        josh.save()

        user_id = josh.id
        sensei = LanguageModel(
            word="Sensei",
            translation="Teacher or Professor",
            example_of_sentence="Nick-san wa sensei desu.",
            part_of_speech="Noun",
            pronunciation="Sen Say",
            user_id=user_id,
        )
        sensei.save()

        user_id = josh.id
        japanese_deck = DeckModel(
            title="Japanese JLPT N5",
            description="N5 Test Study Prep",
            category='Language',
            user_id=user_id,
        )
        japanese_deck.save()

        user_id = josh.id
        medical_deck = DeckModel(
            title="Medical Terminology",
            description="Anatomy Study Prep",
            category="Medical",
            user_id=user_id,
        )
        medical_deck.save()

        deck_id = josh.id
        sample = CardModel(
            front_content="Front of Card Contents",
            back_content="Back of Card Contents",
            deck_id=deck_id,
        )
        sample.save()

        user_id = josh.id
        abdomen = MedicalTermModel(
            term="Abdomen",
            definition="The portion of the body between the thorax and pelvis, containing the stomach, intestines, liver, and other organs.",
            anatomy="Stomach",
            user_id=user_id,
        )
        abdomen.save()

        print("Seeding some data to our database! 🍡")

    except Exception as e:
        print(e)
