from marshmallow import fields
from app import marsh
from models.medical_term import MedicalTermModel
from serializers.user import UserSerializer


class MedicalTermSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = MedicalTermModel
        load_instance = True
