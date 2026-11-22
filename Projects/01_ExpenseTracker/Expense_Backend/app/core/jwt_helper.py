# Functions that help with JWT token generation and validation
from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi import HTTPException, status


SECRET_KEY = "my-super-secret-key"
ALGORITH = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30


# Function to create access tokens
def create_access_token(data: dict, expires_delta: timedelta | None=None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + timedelta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)

    to_encode.update({
        "exp": expire
    })

    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITH)
    return encoded_token


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITH])
        return payload
    except jwt.JWTError:
        print("Invalid token...")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token..."
        )


if __name__ == "__main__":
    print(f"This is main module {__name__}")
    token = create_access_token({"name": "krishna"})
    payload = verify_access_token(token)

    print(token)
    print(payload)
    print("Token verified successfully")

