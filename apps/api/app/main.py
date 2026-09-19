from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://slektskart.no"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}


@router.post("/register")
def register(data: UserCreate):
    # 1. Check email isn't already registered

    # 2. Hash password
    hashed = hash_password(data.password)

    # 3. Create User
    user = User(
        email=data.email,
        password_hash=hashed,
        display_name=data.display_name,
    )

    # 4. Save to database

    # 5. Return safe UserResponse