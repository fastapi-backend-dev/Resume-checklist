from pydantic import BaseModel, EmailStr


class ExpenseRequest(BaseModel):
    title: str
    description: str


class ExpenseResponse(BaseModel):
    title: str
    description: str
    created_date: str
