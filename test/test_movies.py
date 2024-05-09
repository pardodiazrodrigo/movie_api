from .utils import client, test_movie
from .utils import TestingSessionLocal
from database.models import DBMovie


def test_read_all(test_movie):
    response = client.get('/movies')
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "title": "Test Movie",
        "director": "Test Director",
        "release_year": 2022,
        "genre": "Test Genre",
    }]


def test_create(test_movie):
    response = client.post('/movies', json={
        "title": "Test Create Movie",
        "director": "Test Create",
        "release_year": 2000,
        "genre": "Test Create",
    })
    assert response.status_code == 201
    db = TestingSessionLocal()
    movie = db.query(DBMovie).filter_by(id=2).first()
    assert movie.title == "Test Create Movie"
    db.close()


def test_read_one(test_movie):
    response = client.get('/movies/1')
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Test Movie",
        "director": "Test Director",
        "release_year": 2022,
        "genre": "Test Genre",
    }


def test_update(test_movie):
    response = client.put('/movies/1', json={
        "title": "Test Update Movie",
        "director": "Test Update",
        "release_year": 2000,
        "genre": "Test Update",
    })
    assert response.status_code == 204
    db = TestingSessionLocal()
    movie = db.query(DBMovie).filter_by(id=1).first()
    assert movie.title == "Test Update Movie"
    db.close()


def test_delete(test_movie):
    response = client.delete('/movies/1')
    assert response.status_code == 204
    db = TestingSessionLocal()
    movie = db.query(DBMovie).filter_by(id=1).first()
    assert movie is None
    db.close()
