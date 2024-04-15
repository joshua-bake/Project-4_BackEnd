from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g
from models.card import CardModel
from app import db
from serializers.card import CardSerializer


card_serializer = CardSerializer()

router = Blueprint("cards", __name__)


@router.route("/cards", methods=["GET"])
def get_cards():

    cards = db.session.query(CardModel).all()
    return card_serializer.jsonify(cards, many=True)


@router.route("/cards", methods=["POST"])
def post_card():

    card_dictionary = request.json

    try:
        card_model = card_serializer.load(card_dictionary)
        card_model.user_id = g.current_user.id

        card_dictionary.save()

        # ? Need to append the card to the appropriate Deck.

        return card_serializer.jsonify(card_model)
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/cards/<int:card_id>", methods=["PUT"])
def update_single_show(show_id):

    try:
        existing_card = db.session.query(CardModel).get(show_id)

        if not existing_card:
            return {"message": "Card not found"}, HTTPStatus.NOT_FOUND

        card_dictionary = request.json

        card = card_serializer.load(
            card_dictionary, instance=existing_card, partial=True
        )

        db.session.commit()
        return card_serializer.jsonify(card)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/cards/<int:card_id>", methods=["DELETE"])
def remove_show(card_id):

    card_to_delete = db.session.query(CardModel).get(card_id)

    if not card_to_delete:
        return {"message": "Card not found"}, HTTPStatus.NOT_FOUND

    print(g.current_user)

    if card_to_delete.user_id != g.current_user.id:

        return {
            "message": "This is not your card! Go make your own card."
        }, HTTPStatus.UNAUTHORIZED

    card_to_delete.remove()

    return card_serializer.jsonify(card_to_delete)
