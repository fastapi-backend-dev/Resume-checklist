from pydantic import BaseModel, Field
from datetime import datetime


class UserRequestDto(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user")
    email: str = Field(..., max_length=100, description="Email of the user")
    password: str = Field(..., min_length=6, max_length=100, description="Password of the user")


class UserResponseDto(BaseModel):
    id: int = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")
    email: str = Field(..., description="Email of the user")
    created_at: datetime = Field(..., description="Creation date of the user")

    model_config = {
        "from_attributes": True,
    }


class UserUpdateDto(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user")
    email: str = Field(..., max_length=100, description="Email of the user")
    password: str = Field(..., min_length=6, max_length=100, description="Password of the user")