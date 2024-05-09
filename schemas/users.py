from pydantic import BaseModel


class UserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str | None = None
    last_name: str | None = None
    role: str

    model_config = {
        'json_schema_extra': {
            "examples": [{
                "username": "some user",
                "password": "pass",
                "email": "user1@example.com",
                "first_name": "user1",
                "last_name": "example",
                "role": "user"
            }]
        }
    }
