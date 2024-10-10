from fastapi import APIRouter, Response

from auth.schemas import AuthSchema
from auth.service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/registration")
async def register_user(data: AuthSchema):
    await AuthService.register_user(data)


@router.post("/login")
async def login_user(response: Response, data: AuthSchema):
    return await AuthService.login_user(response, data)
