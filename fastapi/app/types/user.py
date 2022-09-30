from typing import List

from app.types.playlist import Playlist


class User:
    def __init__(self, name: str, playlists: List[Playlist]) -> None:
        self.name = name
        self.playlists = playlists

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, User):
            return False

        user: User = __o

        return self.name == user.name and self.playlists == user.playlists
