from marshmallow import fields
from app import marsh
from models.language import LanguageModel
from serializers.user import UserSerializer


class LanguageSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = LanguageModel
        load_instance = True
