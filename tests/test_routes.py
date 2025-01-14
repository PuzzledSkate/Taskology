import pytest
from app import create_app, db
from app.models import Task

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'OK'}

def test_create_task(client):
    response = client.post('/todos', json={'title': 'Test Task'})
    assert response.status_code == 201

def test_get_tasks(client):
    client.post('/todos', json={'title': 'Test Task'})
    response = client.get('/todos')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

