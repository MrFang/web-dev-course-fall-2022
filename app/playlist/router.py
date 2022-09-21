from typing import List

from app.db import db
from app.playlist.types import Playlist
from app.types.playlist import Playlist as PlaylistModel
from app.types.user import User
from fastapi import APIRouter

router = APIRouter(
    prefix='/playlist'
)


@router.get('/list')
def user_playlists(username: str):
    return [
        playlist.name
        for playlist in [
            user.playlists
            for user in db['users']
            if user.name == username
        ][0]
    ]


@router.post('/add')
def add_playlist(playlist: Playlist):
    user: List[User] = [u for u in db['users'] if u.name == playlist.username]
    if (user):
        idx = db['users'].index(user[0])
        db['users'][idx].playlists.append(
            PlaylistModel(playlist.name, playlist.songs)
        )
