from fastapi import APIRouter
from app.api.test import router as test_router
from app.api.user import router as user_router
from app.api.auth import router as auth_router


api_router = APIRouter()
api_router.include_router(test_router, prefix="/test", tags=["Test"])
api_router.include_router(user_router, prefix="/user", tags=["User"])
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])