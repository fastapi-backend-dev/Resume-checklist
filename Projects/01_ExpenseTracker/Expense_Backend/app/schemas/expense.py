from pydantic import BaseModel, Field
from datetime import datetime


class ExpenseRequestDto(BaseModel):
    title: str = Field(..., min_length=2, max_length=100, description="Title of the expense")
    amount: float = Field(..., gt=0, description="Amount of the expense")
    description: str = Field(..., description="Description of the expense")
    show: bool = Field(description="Whether the expense should be shown", default=True)


class ExpenseResponseDto(BaseModel):
    id: int = Field(..., description="ID of the expense")
    title: str = Field(..., description="Title of the expense")
    amount: float = Field(..., description="Amount of the expense")
    description: str = Field(..., description="Description of the expense")
    show: bool = Field(..., description="Whether the expense should be shown")
    created_at: datetime = Field(..., description="Creation date of the expense")

    model_config = {
        "from_attributes": True,
    }
