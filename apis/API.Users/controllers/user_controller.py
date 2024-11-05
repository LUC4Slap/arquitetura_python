from fastapi import APIRouter
from services.user_service import get_users

router = APIRouter()

@router.get("/users/")
async def read_users():
  return await get_users()
