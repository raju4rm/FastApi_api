from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.db.database  import Base
from app.models.enums import StatusEnum
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    user_type_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone_no = Column(String(20), unique=True, nullable=True)
    address = Column(String(1000), nullable=True)
    email_otp = Column(Integer, nullable=True)
    phone_otp = Column(Integer, nullable=True)
    forget_password_token = Column(String(255), nullable=True)
    is_active = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE, nullable=False)
    created_by = Column(Integer, nullable=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_by = Column(Integer, nullable=True)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

