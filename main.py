from fastapi import FastAPI
from database.models import Base
from database.core import engine
from starlette import status
from routers import auth
from routers import movies


app = FastAPI(
    title="Movie API",
    version="1.0.0",
)

app.include_router(auth.router)
app.include_router(movies.router)

Base.metadata.create_all(bind=engine)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "server is running"}
