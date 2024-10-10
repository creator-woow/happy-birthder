from datetime import timedelta, datetime

from fastapi import Request, Response
import jwt

from config import settings
from .const import JWT_EXPIRATION_FIELD


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)) -> str:
    encode_data = data.copy()
    expiration_datetime = datetime.utcnow() + expires_delta
    encode_data.update({JWT_EXPIRATION_FIELD: expiration_datetime})
    access_token = jwt.encode(encode_data, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return access_token


def get_access_token(request: Request) -> str:
    return request.cookies.get(settings.JWT_COOKIE_NAME)


def set_access_token(response: Response, token: str) -> Response:
    response.set_cookie(settings.JWT_COOKIE_NAME, token, httponly=True)
    return response


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
