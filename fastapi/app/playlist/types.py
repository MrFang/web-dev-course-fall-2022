from typing import List

from pydantic import BaseModel


class Playlist(BaseModel):
    username: str
    name: str
    songs: List[str]
