from typing import List, Optional

from app.db import db
from app.playlist.types import Playlist
from app.types.playlist import Playlist as PlaylistModel
from app.types.user import User
from fastapi import APIRouter

router = APIRouter(
    prefix='/playlist'
)


@router.get('/list')
def user_playlists(username: str) -> List[str]:
    user: Optional[User] = next(
        (u for u in db['users'] if u.name == username), None)

    if not user:
        return []

    return [playlist.name for playlist in user.playlists]


@router.post('/add')
def add_playlist(playlist: Playlist) -> None:
    user: User = next(
        (u for u in db['users'] if u.name == playlist.username), None)

    if user:
        idx = db['users'].index(user)
        db['users'][idx].playlists.append(
            PlaylistModel(playlist.name, playlist.songs)
        )
