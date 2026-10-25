import os

from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt

load_dotenv()

JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
TOKEN_ALGORITHM = os.environ["TOKEN_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

def create_access_token(user_id: UUID) -> str:
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": str(user_id),
        "exp": expires_at,
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=TOKEN_ALGORITHM)

def decode_access_token(access_token: str) -> UUID: 
    payload = jwt.decode(access_token, JWT_SECRET_KEY, algorithms=[TOKEN_ALGORITHM])
    subject = payload.get("sub")
    if subject is None:
        raise ValueError("Token has no subject")
    
    return UUID(subject)
    