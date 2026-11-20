from fastapi import FastAPI

from schemas.api import APIResponse

app = FastAPI()


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


@app.put("/users/{user_id}/name/{user_name}")
def update_user(user_id: int, user_name: str):
    return {
        "message": "User updated successfully!!",
        "user_id": user_id,
        "user_name": user_name
    }


@app.get("/users/search")
def search_user(first_name: str="", last_name: str="", city: str=""):
    print(first_name, last_name, city)
    return {
        "data": [],
        "status": True
    }


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
