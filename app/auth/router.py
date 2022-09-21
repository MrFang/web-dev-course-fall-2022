from app.auth.types import User
from app.db import db
from app.types.user import User as UserModel
from fastapi import APIRouter

router = APIRouter(
    prefix='/auth'
)


@router.post('/register')
def register(user: User):
    db['users'].append(UserModel(user.name, []))


@router.get('/list')  # For debug
def list():
    return db['users']
