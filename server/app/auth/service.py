from fastapi import Response, HTTPException, status

from users.service import UserService

from .actions import authenticate_user
from .lib import hash_password, create_access_token, set_access_token, JWT_ID_FIELD
from .schemas import AuthSchema


class AuthService:

    @classmethod
    async def register_user(cls, data: AuthSchema):
        existing_user = await UserService.find_one_or_none(email=data.email)
        if existing_user is not None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Email already registered")
        await UserService.add_one(
            email=data.email,
            hashed_password=hash_password(data.password)
        )

    @classmethod
    async def login_user(cls, response: Response, data: AuthSchema):
        user = await authenticate_user(data)
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        access_token = create_access_token({JWT_ID_FIELD: user.id})
        set_access_token(response, access_token)
        return {"access_token": access_token}
