from app import app, db
import json
from tests.lib import login, setup
import pprint


def test_gets_shows():

    client = app.test_client()

    response = client.get("/api/shows")

    pprint.pp(response.json)

    assert len(response.json) == 2
    assert response.status_code == 200
    assert response.json[0]["name"] == "Master's Daughter"


def test_gets_one_show():

    client = app.test_client()

    response = client.get("/api/shows/2")

    pprint.pp(response.json)

    assert response.status_code == 200
    assert response.json["name"] == "Never Let Me Go"


def test_creates_show():

    client = app.test_client()

    token = login(client)

    show_data = {
        "name": "My Demon",
        "region": "Korea",
        "genre": "Romance",
        "sub_genre": "Comedy",
        "platform": "Netflix",
        "rating": 10,
        "user_id": 1,
    }

    request_headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/shows",
        data=json.dumps(show_data),
        content_type="application/json",
        headers=request_headers,
    )

    print("----------------TEST CREATE SHOW --------------")
    pprint.pp(response.json)
    # assert response.json["name"] == "My Demon"


def test_update_show():

    client = app.test_client()

    token = login(client)

    show_data = {
        "name": "Never Let Me Go",
        "region": "Thailand",
        "genre": "BL",
        "sub_genre": "Action",
        "platform": "Viki",
        "rating": 9,
        "user_id": 1,
    }

    request_headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/shows/2",
        data=json.dumps(show_data),
        content_type="application/json",
        headers=request_headers,
    )

    print("----------------TEST UPDATE SHOW --------------")
    pprint.pp(response.json)
    assert response.json["name"] == "Never Let Me Go"
