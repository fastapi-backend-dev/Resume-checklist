# Auth Routes
from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth_router.post("/login")
def login():
    return {
        "message": "Login successful!!"
    }


@auth_router.post("/register")
def register():
    return {
        "message": "User registered successfully!!"
    }
