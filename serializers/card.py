from marshmallow import fields
from app import marsh
from models.card import CardModel
from serializers.user import UserSerializer


class CardSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = CardModel
        load_instance = True
