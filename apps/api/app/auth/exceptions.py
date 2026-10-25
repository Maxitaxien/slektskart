from fastapi import HTTPException, status

credentials_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail="Kunne ikke validere innlogging",
    headers={"WWW-Authenticate": "Bearer"},
) 