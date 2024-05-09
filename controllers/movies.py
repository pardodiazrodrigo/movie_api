from fastapi import HTTPException
from database.models import DBMovie
from schemas.movies import MovieRequest


async def user_permissions(user):
    if user["role"] not in ['user', 'admin'] or user is None:
        raise HTTPException(
            status_code=403,
            detail=f"Permission denied. Only users have access to this operation.",
        )


async def admin_permissions(user):
    if user["role"] != 'admin' or user is None:
        raise HTTPException(
            status_code=403,
            detail=f"Permission denied. Only admins have access to this operation.",
        )


async def get_movie(db, movie_id: int):
    movie_model = db.query(DBMovie).filter(DBMovie.id == movie_id).first()
    if movie_model is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_model


async def read_all_movies(user, db):
    await user_permissions(user)
    return db.query(DBMovie).all()


async def create_movie(user, db, movie_request: MovieRequest):
    await admin_permissions(user)
    movie = DBMovie(**movie_request.dict())
    db.add(movie)
    db.commit()


async def read_movie(user, db, movie_id: int):
    await user_permissions(user)
    return await get_movie(db, movie_id)


async def update_movie(user, db, movie_request: MovieRequest, movie_id: int):
    await admin_permissions(user)
    movie_model = await get_movie(db, movie_id)
    movie_model.title = movie_request.title
    movie_model.release_year = movie_request.release_year
    movie_model.director = movie_request.director
    movie_model.genre = movie_request.genre
    db.add(movie_model)
    db.commit()


async def delete_movie(user, db, movie_id: int):
    await admin_permissions(user)
    movie_model = await get_movie(db, movie_id)
    db.delete(movie_model)
    db.commit()
