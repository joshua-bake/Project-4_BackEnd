from http import HTTPStatus
from functools import wraps
from flask import request, g
import jwt
from app import db
from models.user import UserModel
from config.environment import SECRET


def secure_route(route_func):

    @wraps(route_func)
    def wrapper(*args, **kwargs):

        raw_token = request.headers.get("Authorization")
        print(raw_token)

        if not raw_token:
            print("Token is not there.")
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        token = raw_token.replace("Bearer ", "")
        print(token)

        try:
            payload = jwt.decode(token, SECRET, "HS256")

            print("Token was valid")

            user_id = payload["sub"]

            user = db.session.query(UserModel).get(user_id)

            g.current_user = user

            print("current user is: ", g.current_user.username, g.current_user)

            return route_func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            print("Expired")
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED
        except Exception:
            print("Issue with token")
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

    return wrapper
