from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from schemas.token import Token
from schemas.users import UserRequest
from database.models import DBUser
from database.core import db_dependency
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm
from controllers.auth import bcrypt_context, authenticate_user, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    user = DBUser(
        email=user_request.email,
        username=user_request.username,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        role=user_request.role,
        hashed_password=bcrypt_context.hash(user_request.password),
        is_active=True,
    )
    db.add(user)
    db.commit()


@router.post("/token", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user.",
        )

    token = create_access_token(
        user.username, user.id, user.role, timedelta(minutes=20)
    )

    return {"access_token": token, "token_type": "bearer"}
