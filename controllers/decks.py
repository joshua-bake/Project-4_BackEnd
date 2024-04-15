from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g
from models.deck import DeckModel
from app import db
from serializers.deck import DeckSerializer


deck_serializer = DeckSerializer()

router = Blueprint("decks", __name__)


@router.route("/decks", methods=["GET"])
def get_decks():

    decks = db.session.query(DeckModel).all()
    return deck_serializer.jsonify(decks, many=True)


@router.route("/decks", methods=["POST"])
def create_decks():

    deck_dictionary = request.json

    try:
        deck_model = deck_serializer.load(deck_dictionary)
        deck_model.user_id = g.current_user.id

        deck_model.save()

        return deck_serializer.jsonify(deck_model)
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong.",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong."}, HTTPStatus.INTERNAL_SERVER_ERROR
