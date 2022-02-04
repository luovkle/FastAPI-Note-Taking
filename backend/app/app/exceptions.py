from fastapi import HTTPException, status


class Exceptions:
    USERNAME_UNAVAILABLE = HTTPException(
        detail="Username is not available",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    EMAIL_UNAVAILABLE = HTTPException(
        detail="Email is not available",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    CREDENTIALS_EXCEPTION = HTTPException(
        detail="Could not validate credentials",
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"},
    )
    TITLE_UNAVAILABLE = HTTPException(
        detail="Title is not available",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    NOTE_NOT_FOUND = HTTPException(
        detail="The note does not exist",
        status_code=status.HTTP_404_NOT_FOUND,
    )


exceptions = Exceptions()
