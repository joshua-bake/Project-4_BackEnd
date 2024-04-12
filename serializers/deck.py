from marshmallow import fields
from app import marsh
from models.deck import DeckModel
from serializers.user import UserSerializer


class DeckSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = DeckModel
        load_instance = True
