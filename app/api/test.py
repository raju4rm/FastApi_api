from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.schemas.test_layout_2 import Create
from sqlalchemy.orm import Session
from app.models.test_layout2 import TestLayout2
from app.utils.response import send_success_response,send_error_response
from fastapi import HTTPException

router = APIRouter()

@router.post("/test")
def test():
    return "Test Post"

@router.get("/test")
def test():
    return "Test Get 1"

@router.post("/test-layout-2")
def test_layout_2(data: Create, db: Session = Depends(get_db)):
    try:
        new_entry = TestLayout2(
            input_box1=data.input_box,
            select_box=data.select_box
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)

        return send_success_response(
            "Test Layout 2 entry created successfully.",
            status_code=200
        )
    except Exception as e:
        db.rollback()
        return send_error_response(
            message="Server Error! Please try again later.",
            errors=str(e),
            status_code=500
        )
        
