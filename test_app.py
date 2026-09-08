import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"hello world"


def test_success(client):
    response = client.get("/success/80")

    assert response.status_code == 200
    assert b"person has passed with score 80" in response.data


def test_form_get(client):
    response = client.get("/form")

    assert response.status_code == 200


def test_form_post(client):
    response = client.post(
        "/form",
        data={
            "maths": "80",
            "science": "70",
            "kannada": "90"
        }
    )

    assert response.status_code == 200

    # Average = (80 + 70 + 90) / 3 = 80
    assert b"80" in response.data