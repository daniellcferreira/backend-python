import pytest
from src.app import create_app, db

@pytest.fixture()
def app():
    app = create_app(environment="testing")
    with app.app_context():
        db.create_all()
        yield app

@pytest.fixture()
def client(app):
    return app.test_client()
