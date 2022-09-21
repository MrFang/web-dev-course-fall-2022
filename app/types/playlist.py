from typing import List


class Playlist:
    def __init__(self, name: str, songs: List[str]) -> None:
        self.name = name
        self.songs = songs

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Playlist):
            return False

        playlist: Playlist = __o

        return self.name == playlist.name and self.songs == playlist.songs
