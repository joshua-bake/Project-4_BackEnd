import json
import pytest
from app import app, db
from models.base import BaseModel
from models.user import UserModel
import pprint


@pytest.fixture(autouse=True)
def setup():
    with app.app_context():
        try:

            db.create_all()

            user_list = UserModel(
                username="Josh", email="josh@admin.com", password="joshua123"
            )

            # shows_list = [
            #     ShowModel(
            #         name="Master's Daughter",
            #         region="Japan",
            #         genre="Thriller & Suspense",
            #         sub_genre="Crime & Mystery",
            #         platform="Viki",
            #         rating=7.3,
            #         user_id=1,
            #     ),
            #     ShowModel(
            #         name="Never Let Me Go",
            #         region="Thailand",
            #         genre="BL",
            #         sub_genre="Action",
            #         platform="Viki",
            #         rating=8.4,
            #         user_id=1,
            #     ),
            # ]

            user_list.save()
            # db.session.add_all(shows_list)
            # db.session.commit()

            yield

            db.drop_all()

            print("Goodbye!!!🪐")

        except Exception as e:
            print("There was an error.")
            print(e)


def login(client):

    login_data = {"email": "josh@admin.com", "password": "joshua123"}

    response = client.post(
        "/api/login", data=json.dumps(login_data), content_type="application/json"
    )

    print("------------TEST LOGIN-------------")
    pprint.pp(response.json)

    return response.json["token"]
