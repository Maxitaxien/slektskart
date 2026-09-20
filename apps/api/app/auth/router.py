from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.user import UserResponse, UserCreate
from app.models.user import User
from app.auth.dependencies import get_db
from app.auth.hashing import hash_password

router = APIRouter(prefix="/api/auth", tags=["auth"])


# TODO: JWT, verification
@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserCreate, db: Session = Depends(get_db)):
    # 1. Check email isn't already registered
    existing_user = db.scalar(
        select(User).where(User.email == data.email)
    )

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")

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