from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.user import UserResponse, UserCreate 
from app.schemas.auth import UserLogin, TokenResponse
from app.models.user import User
from app.auth.dependencies import get_current_user, get_db
from app.auth.hashing import hash_password, verify_password
from app.auth.tokens import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


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

@router.post("/login", response_model=TokenResponse, status_code=200)
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.scalar(
        select(User).where(User.email == data.email)
    )

    if user is None or not user.is_active or not(verify_password(data.password, user.password_hash)):
        raise HTTPException(status_code=401, detail="Feil epost eller passord")

    return TokenResponse(
        access_token=create_access_token(user.id),
    )


@router.get("/me", response_model=UserResponse)
def read_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user