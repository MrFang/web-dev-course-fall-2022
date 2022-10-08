from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.playlist.router import router as playlist_router
from app.songs.router import router as songs_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(playlist_router)
app.include_router(songs_router)
