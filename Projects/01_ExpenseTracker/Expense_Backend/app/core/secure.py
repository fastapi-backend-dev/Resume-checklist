from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from core.db import get_db

security_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_current_user(request: Request, token: str = Depends(security_scheme), db: Session = Depends(get_db)):
    from core.jwt_helper import verify_access_token
    from models.user import User


    """
    Dependency function to get the current user from the request.
    It extracts the token from the request and verifies it.
    If the token is invalid, it raises an HTTPException.
    """
    try:
        # Verify the token and extract user information
        payload = verify_access_token(token)
        email = payload.get("email")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Fetch the user from the database using the email
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        request.state.user = user  # Store the user in the request state for later use

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
