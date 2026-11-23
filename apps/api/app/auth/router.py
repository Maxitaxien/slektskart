import os

from dotenv import load_dotenv

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.user import UserResponse, UserCreate 
from app.schemas.auth import UserLogin
from app.models.user import User
from app.auth.dependencies import get_current_user, get_db
from app.auth.hashing import hash_password, verify_password
from app.auth.tokens import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])

load_dotenv()

SECURE_TOKEN_COOKIE = bool(os.getenv("SECURE_TOKEN_COOKIE", True))
MAX_AGE = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")) * 60 # convert to seconds for max_age


@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserCreate, db: Session = Depends(get_db)):
    # 1. Check email isn't already registered
    existing_user = db.scalar(
        select(User).where(User.email == data.email)
    )

    if existing_user:
        raise HTTPException(status_code=409, detail="Epost allerede registrert")

    # 2. Hash password
    hashed = hash_password(data.password)

    # 3. Create User
    user = User(
        email=data.email,
        password_hash=hashed,
        display_name=data.display_name,
    )

    # 4. Save to database
    db.add(user)
    db.commit()
    db.refresh(user)

    # 5. Return safe UserResponse
    return UserResponse(
        id=user.id,
        email=user.email,
        display_name=user.display_name,
        is_active=user.is_active,
        email_verified=user.email_verified
    )

@router.post("/login", status_code=200)
def login(data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.scalar(
        select(User).where(User.email == data.email)
    )

    if user is None or not user.is_active or not(verify_password(data.password, user.password_hash)):
        raise HTTPException(status_code=401, detail="Feil epost eller passord")

    token = create_access_token(user.id)

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=SECURE_TOKEN_COOKIE,
        samesite="lax",
        path="/",
        max_age=MAX_AGE
    )

    return {"message": "Login successful"}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        path="/"
    )

    return {
        "message": "Logged out successfully"
    }

@router.get("/me", response_model=UserResponse)
def read_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user