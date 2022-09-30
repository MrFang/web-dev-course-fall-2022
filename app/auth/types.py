from pydantic import BaseModel


class User(BaseModel):
    name: str
    password: str  # TODO: auth mechanism
