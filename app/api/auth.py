from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
router = APIRouter()

from app.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.utils.security import hash_password
from app.utils.response import send_success_response, send_error_response, send_records_response
from fastapi.encoders import jsonable_encoder

@router.post("/sign-up")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            return send_error_response(
                message="User with this email already exists.",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        new_user = User(
            user_type_id=1,
            name=user.name,
            username=user.email,
            email=user.email,
            phone_no=user.phone_no,
            password=hash_password(user.password),
            is_active="ACTIVE"
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return send_success_response(
            message="User registered successfully.",
            status_code=status.HTTP_201_CREATED
        );
    except Exception as e:
        db.rollback()
        return send_error_response(
            message="Internal server error",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    

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