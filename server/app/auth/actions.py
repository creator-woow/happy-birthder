from users.schemas import UserSchema
from users.service import UserService

from .lib import verify_password
from .schemas import AuthSchema


async def authenticate_user(data: AuthSchema) -> UserSchema | None:
    user = await UserService.find_one_or_none(email=data.email)
    if not user or not verify_password(data.password, user.hashed_password):
       return None
    return user
