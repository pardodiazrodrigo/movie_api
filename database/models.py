from .core import Base
from sqlalchemy import Column, Integer, String, Boolean


class DBMovie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    release_year = Column(Integer)
    director = Column(String)
    genre = Column(String)
    # main_actors = Column(ARRAY(String))


class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
