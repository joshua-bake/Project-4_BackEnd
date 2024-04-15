from app import app, db
import json
from tests.lib import login, setup
import pprint


def test_gets_users():

    client = app.test_client()

    response = client.get("/api/users")

    pprint.pp(response.json)


def test_sign_up():

    client = app.test_client()

    sign_up_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testinguser123",
    }

    response = client.post(
        "/api/signup", data=json.dumps(sign_up_data), content_type="application/json"
    )

    pprint.pp(response.json)
