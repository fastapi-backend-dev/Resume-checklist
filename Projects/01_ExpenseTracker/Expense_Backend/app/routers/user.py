from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.db import get_db
from core.security import hash_password, verify_password
from schemas.api_response import APIResponse
from schemas.user import UserRequestDto, UserResponseDto, UserUpdateDto
from models.user import User

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# Create a new user
@user_router.post("/", response_model=APIResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_request_dto: UserRequestDto, db: Session = Depends(get_db)):
    # Check if the username already exists
    existing_user = db.query(User).filter(User.username == user_request_dto.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    # Check if the email already exists
    existing_email = db.query(User).filter(User.email == user_request_dto.email).first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    # Hash the password before storing it in the database
    hashed_password = hash_password(user_request_dto.password)

    # Create the new user
    new_user = User(
        username=user_request_dto.username,
        email=user_request_dto.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return APIResponse(
        status="success",
        message="User created successfully",
        data={"user": UserResponseDto.model_validate(new_user)}
    )


# Get all users
@user_router.get("/", response_model=APIResponse, status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return APIResponse(
        status="success",
        message="Users retrieved successfully",
        data={"users": [UserResponseDto.model_validate(user) for user in users]}
    )


# Get a specific user by ID
@user_router.get("/{user_id}", response_model=APIResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return APIResponse(
        status="success",
        message="User retrieved successfully",
        data={"user": UserResponseDto.model_validate(user)}
    )


# Update a user by ID
@user_router.put("/{user_id}", response_model=APIResponse)
def update_user(user_id: int, user_update_dto: UserUpdateDto, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Check unique constraints if fields are updated
    if user_update_dto.username and user_update_dto.username != user.username:
        conflict = db.query(User).filter(User.username == user_update_dto.username).first()
        if conflict:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
        user.username = user_update_dto.username

    if user_update_dto.email and user_update_dto.email != user.email:
        conflict = db.query(User).filter(User.email == user_update_dto.email).first()
        if conflict:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        user.email = user_update_dto.email

    if user_update_dto.password:
        # Hash the new password before storing it in the database
        user.password = hash_password(user_update_dto.password)
        
    db.commit()
    db.refresh(user)
    return APIResponse(
        status="success",
        message="User updated successfully",
        data={"user": UserResponseDto.model_validate(user)}
    )


# Delete a user by ID
@user_router.delete("/{user_id}", response_model=APIResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return APIResponse(
        status="success",
        message="User deleted successfully",
        data=None
    )
