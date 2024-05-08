from pydantic import BaseModel


class UserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str | None = None
    last_name: str | None = None
    role: str
