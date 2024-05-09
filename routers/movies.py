from fastapi import APIRouter
from starlette import status
from database.core import db_dependency
from database.models import DBMovie
from fastapi import HTTPException, Path
from schemas.movies import MovieRequest
from controllers.auth import user_dependency
from controllers.movies import read_all_movies, create_movie, read_movie, update_movie, delete_movie

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(
    user: user_dependency,
    db: db_dependency,
):
    return await read_all_movies(user, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user: user_dependency, db: db_dependency, movie_request: MovieRequest):
    return await create_movie(user, db, movie_request)


@router.get("/{movie_id}", status_code=status.HTTP_200_OK)
async def read(user: user_dependency, db: db_dependency, movie_id: int = Path(gt=0)):
    return await read_movie(user, db, movie_id)


@router.put("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update(
    user: user_dependency,
    db: db_dependency,
    movie_request: MovieRequest,
    movie_id: int = Path(gt=0),
):
    return await update_movie(user, db, movie_request, movie_id)


@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user: user_dependency, db: db_dependency, movie_id: int = Path(gt=0)):
    return await delete_movie(user, db, movie_id)
