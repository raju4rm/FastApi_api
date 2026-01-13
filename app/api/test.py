from fastapi import APIRouter
router = APIRouter()

@router.post("/test")
def test():
    return "Test Post"

@router.get("/test")
def test():
    return "Test Get 1"
