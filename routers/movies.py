from fastapi import APIRouter
from starlette import status
from database.core import db_dependency
from database.models import DBMovie
from fastapi import HTTPException, Path
from schemas.movies import MovieRequest
from controllers.auth import user_dependency

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(
    user: user_dependency,
    db: db_dependency,
):
    if user["role"] not in ["admin", "user"]:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. Only users have access to this operation.",
        )
    return db.query(DBMovie).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user: user_dependency, db: db_dependency, movie_request: MovieRequest):
    if user["role"] != "admin" or user is None:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. Only admin users have access to this operation.",
        )
    movie = DBMovie(**movie_request.dict())
    db.add(movie)
    db.commit()


@router.get("/{movie_id}", status_code=status.HTTP_200_OK)
async def read(user: user_dependency, db: db_dependency, movie_id: int = Path(gt=0)):
    if user["role"] not in ["admin", "user"]:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. Only users have access to this operation.",
        )
    movie_model = db.query(DBMovie).filter(DBMovie.id == movie_id).first()
    if movie_model is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_model


@router.put("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update(
    user: user_dependency,
    db: db_dependency,
    movie_request: MovieRequest,
    movie_id: int = Path(gt=0),
):
    if user["role"] != "admin" or user is None:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. Only admin users have access to this operation.",
        )
    movie_model = db.query(DBMovie).filter(DBMovie.id == movie_id).first()
    if movie_model is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_model.title = movie_request.title
    movie_model.release_year = movie_request.release_year
    movie_model.director = movie_request.director
    movie_model.genre = movie_request.genre
    db.add(movie_model)
    db.commit()


@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user: user_dependency, db: db_dependency, movie_id: int = Path(gt=0)):
    movie_model = db.query(DBMovie).filter(DBMovie.id == movie_id).first()
    if user["role"] != "admin" or user is None:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. Only admin users have access to this operation.",
        )
    if movie_model is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie_model)
    db.commit()
