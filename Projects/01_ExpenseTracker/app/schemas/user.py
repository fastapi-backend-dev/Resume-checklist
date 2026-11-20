from pydantic import BaseModel, Field


class UserDto(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=10)
    last_name: str
    city: str
    age: int
    is_active: bool = True
