from fastapi import FastAPI, Depends, status, HTTPException

from schemas.api import APIResponse
from schemas.user import UserDto
from routers.auth import auth_router
from routers.user import user_router

app = FastAPI(
    title="FastAPI Demo",
    description="This is a demo FastAPI application",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI"
    }

app.include_router(auth_router)
app.include_router(user_router)

# @app.get("/users")
# def get_users():
#     return [
#         "Krishna",
#         "Kalyan",
#         "Gokul",
#         "Ganesh"
#     ]



# @app.post("/users", response_model=APIResponse)
# def create_new_user():
#     return APIResponse(
#         message="User created successfully!!",
#         status="OK",
#         success=True
#     )


def get_token():
    print("Getting token from DB...")
    return "This is a token"


# @app.put("/users/{user_id}/name/{user_name}")
# def update_user(user_id: int, user_name: str):
#     return {
#         "message": "User updated successfully!!",
#         "user_id": user_id,
#         "user_name": user_name
#     }


# @app.get("/users/search")
# def search_user(first_name: str="", last_name: str="", city: str=""):
#     print(first_name, last_name, city)
#     return {
#         "data": [],
#         "status": True
#     }


# @app.post("/users", status_code=status.HTTP_201_CREATED)
# def create_user(user: UserDto, token: str=Depends(get_token)):
#     print(f"First Name: {user.first_name}, Last Name: {user.last_name}, City: {user.city}, Age: {user.age}, Is Active: {user.is_active}")

#     if user.first_name == "abc":
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="First name cannot be abc"
#         )

#     return {
#         "message": "User created successfully!!",
#         "user": user,
#         "token": token
#     }


# @app.get("/", response_model=APIResponse)
# def home():
#     return APIResponse(
#         message="This is through API response",
#         success=True,
#         status="OK"
#     )


# @app.get("/get-users")
# def get_users():
#     return [
#         "Krishna",
#         "Kalyan",
#         "Gokul",
#         "Ganesh"
#     ]
