from fastapi import FastAPI

from schemas.api import APIResponse

app = FastAPI()


@app.get("/", response_model=APIResponse)
def home():
    return APIResponse(
        message="This is through API response",
        success=True,
        status="OK"
    )


@app.get("/get-users")
def get_users():
    return [
        "Krishna",
        "Kalyan",
        "Gokul",
        "Ganesh"
    ]
