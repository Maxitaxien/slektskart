from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    display_name: str | None = None


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    display_name: str | None
    is_active: bool
    email_verified: bool

    model_config = {
        "from_attributes": True,
    }