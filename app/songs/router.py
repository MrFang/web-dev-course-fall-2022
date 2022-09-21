from typing import List

from app.db import db
from app.types.user import User
from fastapi import APIRouter

router = APIRouter(
    prefix='/song'
)


@router.get('/list')
def get_user_songs(username: str) -> List[str]:
    user: List[User] = [u for u in db['users'] if u.name == username]

    if not user:
        return []

    songs: List[str] = []

    for p in user[0].playlists:
        for s in p.songs:
            songs.append(s)

    return songs
