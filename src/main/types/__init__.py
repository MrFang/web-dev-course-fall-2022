
from pydantic import BaseModel


class RequestBody(BaseModel):
    value: str
