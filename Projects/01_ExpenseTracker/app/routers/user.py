# API Routers for user
from fastapi import APIRouter

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@user_router.get("")
def get_users():
    pass


@user_router.post("")
def create_new_user():
    pass


@user_router.put("{user_id}")
def update_user(user_id: int):
    pass