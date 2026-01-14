from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
router = APIRouter()

from app.schemas.user import UserCreate, SignInRequest
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.utils.security import hash_password, verify_password
from app.utils.response import send_success_response, send_error_response, send_records_response
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
from app.utils.jwt import create_access_token

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

@router.post("/sign-in")
def signin(user : SignInRequest, db: Session = Depends(get_db)):
    try:
        check = db.query(User).filter(User.email == user.email).first()

        if check and verify_password(user.password, check.password):
            access_token = create_access_token(
                data={
                    "user_id": str(check.user_id),
                    "email": check.email
                },
                expires_delta=timedelta(minutes=60)
            )

            data = {
                "user_id": check.user_id,
                "email": check.email,
                "name": check.name,
                "access_token": access_token
            }

            return send_records_response(
                message ="Sign-in successful1.", 
                data = data,
                total_count = 1,
                status_code = status.HTTP_200_OK
            )
        else:
            return send_error_response(
                message = "Invalid email or password.",
                errors = {"email": "Invalid email or password."},
                status_code =status.HTTP_401_UNAUTHORIZED
            )
    except Exception as e:
        return send_error_response(
            message = "Internal server error",
            errors = str(e),
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        )
            

   