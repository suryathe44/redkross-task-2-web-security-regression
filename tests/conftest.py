import pytest
from app.app import create_app

@pytest.fixture()
def client():
    app = create_app({"TESTING": True, "SECRET_KEY": "pytest-only-secret"})
    with app.test_client() as client:
        yield client
