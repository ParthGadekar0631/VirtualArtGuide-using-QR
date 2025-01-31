import pytest
from app.routes import app

@pytest.fixture
def client():
    """
    Flask test client fixture.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """
    Test the home route.
    """
    response = client.get("/")
    assert response.status_code == 200, "Home route did not return status 200."
    assert b"Welcome to Virtual Art Guide" in response.data, "Homepage content is incorrect."
