from fastapi import APIRouter

from users.schemas import UserSchema
from users.service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
async def get_users() -> list[UserSchema]:
    return await UserService.find_all()


@router.get("/{user_id}")
async def get_user(user_id: int) -> UserSchema:
    return await UserService.find_by_id(user_id)
