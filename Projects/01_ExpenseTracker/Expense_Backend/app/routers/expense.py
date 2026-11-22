from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.db import get_db
from schemas.api_response import APIResponse
from schemas.expense import ExpenseRequestDto, ExpenseResponseDto
from models.expense import Expense
from core.secure import get_current_user
from models.user import User

expense_router = APIRouter(
    prefix="/expenses",
    tags=["expenses"]
)


# Create a new expense
@expense_router.post("/", response_model=APIResponse, status_code=status.HTTP_201_CREATED)
def create_expense(expense_request_dto: ExpenseRequestDto, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    new_expense = Expense(
        title=expense_request_dto.title,
        amount=expense_request_dto.amount,
        description=expense_request_dto.description,
        show=expense_request_dto.show
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return APIResponse(
        status="success",
        message="Expense created successfully",
        data={"expense": ExpenseResponseDto.model_validate(new_expense)}
    )


# Get all expenses
@expense_router.get("/", response_model=APIResponse, status_code=status.HTTP_200_OK)
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return APIResponse(
        status="success",
        message="Expenses retrieved successfully",
        data={"expenses": [ExpenseResponseDto.model_validate(expense) for expense in expenses]}
    )


# Get a specific expense by ID
@expense_router.get("/{expense_id}", response_model=APIResponse, status_code=status.HTTP_200_OK)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    return APIResponse(
        status="success",
        message="Expense retrieved successfully",
        data={"expense": ExpenseResponseDto.model_validate(expense)}
    )


# Update an expense by ID
@expense_router.put("/{expense_id}", response_model=APIResponse)
def update_expense(expense_id: int, expense_request_dto: ExpenseRequestDto, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    expense.title = expense_request_dto.title
    expense.amount = expense_request_dto.amount
    expense.description = expense_request_dto.description
    expense.show = expense_request_dto.show
    db.commit()
    db.refresh(expense)
    return APIResponse(
        status="success",
        message="Expense updated successfully",
        data={"expense": ExpenseResponseDto.model_validate(expense)}
    )


# Delete an expense by ID
@expense_router.delete("/{expense_id}", response_model=APIResponse)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return APIResponse(
        status="success",
        message="Expense deleted successfully"
    )


# Search expenses by title
@expense_router.get("/search/", response_model=APIResponse, status_code=status.HTTP_200_OK)
def search_expenses(title: str, db: Session = Depends(get_db)):
    expenses = db.query(Expense).filter(Expense.title.ilike(f"%{title}%")).all()
    return APIResponse(
        status="success",
        message="Expenses retrieved successfully",
        data={"expenses": [ExpenseResponseDto.model_validate(expense) for expense in expenses]}
    )
