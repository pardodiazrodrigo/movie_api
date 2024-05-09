from pydantic import BaseModel, Field


class MovieRequest(BaseModel):
    title: str = Field(min_length=3)
    release_year: int = Field(gt=1900, lt=2040)
    director: str = Field(min_length=3)
    genre: str = Field(min_length=1)
    # main_actors: List[str]

    model_config = {
        'json_schema_extra': {
            "examples": [{
                'title': 'some title',
                'release_year': 2000,
                'director': 'some director',
                'genre': 'some genre',
            }]
        }
    }
