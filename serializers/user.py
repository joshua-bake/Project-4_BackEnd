from marshmallow import fields, ValidationError
from app import marsh
from models.user import UserModel


def validate_password(password):

    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    if not password.isalnum():
        raise ValidationError(
            "Password must contain at least one letter and one number"
        )
    return


class UserSerializer(marsh.SQLAlchemyAutoSchema):

    password = fields.String(required=True, validate=validate_password)

    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("password", "password_hash", "email")
