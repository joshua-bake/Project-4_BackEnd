from http import HTTPStatus
from datetime import datetime, timezone, timedelta
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request
import jwt
from models.user import UserModel
from app import db
from serializers.user import UserSerializer
from config.environment import SECRET

user_serializer = UserSerializer()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup():

    try:
        user_dictionary = request.json

        user_model = user_serializer.load(user_dictionary)

        user_model.save()

        print("user model", user_model.password)

        return user_serializer.jsonify(user_model)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/login", methods=["POST"])
def login():

    credentials_dictionary = request.json

    user = (
        db.session.query(UserModel)
        .filter_by(email=credentials_dictionary["email"])
        .first()
    )

    if not user:
        return {"message": "Invalid credentials. Try again."}, HTTPStatus.UNAUTHORIZED

    if not user.validate_password(credentials_dictionary["password"]):
        return {"message": "Invalid credentials. Try again."}, HTTPStatus.UNAUTHORIZED

    now_utc = datetime.now(timezone.utc)

    payload = {
        "exp": now_utc + timedelta(days=1),
        "iat": now_utc,
        "sub": user.id,
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    return {"message": "Logged in successfully!", "token": token}


@router.route("/users", methods=["GET"])
def get_users():

    users = db.session.query(UserModel).all()
    return user_serializer.jsonify(users, many=True)


@router.route("/users/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    user = db.session.query(UserModel).get(user_id)

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    return user_serializer.jsonify(user)


@router.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    try:
        user_to_delete = db.session.query(UserModel).get(user_id)

        if not user_to_delete:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        db.session.delete(user_to_delete)
        db.session.commit()

        return user_serializer.jsonify(user_to_delete)
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
