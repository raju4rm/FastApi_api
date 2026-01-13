from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
router = APIRouter()

from app.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.utils.response import send_success_response, send_error_response, send_records_response
from fastapi.encoders import jsonable_encoder


@router.get("/list")
def list(db: Session = Depends(get_db)):
    try:
        users = db.query(User.email,User.name).all()
        data = []
        for user in users:
            data.append({
                "email": user.email,
                "name": user.name
            })

            
        return send_records_response(
            message="User list fetched successfully.",
            data= jsonable_encoder(data),
            total_count=len(data),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        return send_error_response(
            message="Internal server error",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )