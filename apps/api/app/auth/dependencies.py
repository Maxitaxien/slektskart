from typing import Annotated

from app.database import SessionLocal
from app.models.user import User
from fastapi import Depends, Cookie
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from app.auth.tokens import decode_access_token
from app.auth.exceptions import credentials_exception

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
        db: Annotated[Session, Depends(get_db)],
        access_token: str | None = Cookie(default=None)
    ) -> User:
    if not access_token:
        raise credentials_exception
    
    try:
        user_id = decode_access_token(access_token)
    except (InvalidTokenError, ValueError):
        raise credentials_exception

    user = db.get(User, user_id)

    if user is None or not user.is_active:
        raise credentials_exception

    return user