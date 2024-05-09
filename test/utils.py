from decouple import config
from database.models import Base
from database.core import get_db
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from main import app
from controllers.auth import get_current_user
from fastapi.testclient import TestClient
import pytest
from database.models import DBMovie

engine = create_engine(config('TEST_DATABASE_URL'))

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'id': 1, 'username': 'admin', 'role': 'admin'}


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)


@pytest.fixture
def test_movie():
    movie = DBMovie(
        title='Test Movie',
        director='Test Director',
        release_year=2022,
        genre='Test Genre'
    )
    db = TestingSessionLocal()
    db.add(movie)
    db.commit()
    yield movie
    with engine.connect() as conn:
        conn.execute(text(f'TRUNCATE TABLE movies RESTART IDENTITY CASCADE'))
        conn.commit()
