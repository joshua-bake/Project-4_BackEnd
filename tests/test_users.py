from app import app, db
import json
from tests.lib import login, setup
import pprint


def test_gets_users():

    client = app.test_client()

    response = client.get("/api/users")

    pprint.pp(response.json)
