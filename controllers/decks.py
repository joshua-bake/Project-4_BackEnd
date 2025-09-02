from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g
from models.deck import DeckModel
from models.card import CardModel
from app import db
from middleware.secure_route import secure_route
from serializers.deck import DeckSerializer
from serializers.card import CardSerializer


deck_serializer = DeckSerializer()
card_serializer = CardSerializer()

router = Blueprint("decks", __name__)


@router.route("/decks", methods=["GET"])
def get_decks():

    decks = db.session.query(DeckModel).all()
    serialized_decks = deck_serializer.dump(decks, many=True)

    # Iterate over each deck and fetch the associated cards
    for deck_data in serialized_decks:
        deck_id = deck_data["id"]
        cards = db.session.query(CardModel).filter_by(deck_id=deck_id).all()
        serialized_cards = [card_serializer.dump(card) for card in cards]
        deck_data["cards"] = serialized_cards
    return serialized_decks


@router.route("/decks/<int:deck_id>", methods=["GET"])
def get_single_deck(deck_id):
    deck = db.session.query(DeckModel).get(deck_id)

    return deck_serializer.jsonify(deck)


@router.route("/decks", methods=["POST"])
@secure_route
def create_decks():

    deck_dictionary = request.json

    try:
        deck_model = deck_serializer.load(deck_dictionary)
        deck_model.user_id = g.current_user.id

        deck_model.save()

        print("Deck", deck_model, "added")
        return deck_serializer.jsonify(deck_model)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong.",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong."}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/decks/<int:deck_id>", methods=["PUT"])
@secure_route
def update_deck(deck_id):

    try:

        existing_deck = db.session.query(DeckModel).get(deck_id)

        if not existing_deck:
            return {"message": "No deck found"}, HTTPStatus.NOT_FOUND

        if existing_deck.user_id != g.current_user.id:
            return {
                "message": "This is not your deck! Go make your own deck."
            }, HTTPStatus.UNAUTHORIZED

        deck_dictionary = request.json

        deck = deck_serializer.load(
            deck_dictionary,
            instance=existing_deck,
            partial=True,
        )

        db.session.commit()

        return deck_serializer.jsonify(deck)
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/decks/<int:deck_id>", methods=["DELETE"])
@secure_route
def remove_deck(deck_id):
    try:
        deck_to_delete = db.session.query(DeckModel).get(deck_id)

        if not deck_to_delete:
            return {"message": "No deck found"}, HTTPStatus.NOT_FOUND

        if deck_to_delete.user_id != g.current_user.id:
            return {
            "message": "This is not your deck! Go make your own deck."
        }, HTTPStatus.UNAUTHORIZED

        deck_to_delete.remove()

        print("Deck deleted ...", deck_to_delete)
        return {"message": "Deck deleted."}
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR
