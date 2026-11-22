from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.db import get_db
from schemas.user import LoginRequest, LoginResponse, UserResponseDto
from models.user import User
from core.jwt_helper import create_access_token
from core.security import verify_password

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@auth_router.post("/", response_model=LoginResponse)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_request.email).first()

    if not user or not verify_password(login_request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    access_token = create_access_token({"user_id": user.id, "email": user.email})
    return LoginResponse(access_token=access_token, user=UserResponseDto.model_validate(user))
