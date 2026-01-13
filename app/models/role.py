from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.db.database  import Base
from app.models.enums import StatusEnum
from sqlalchemy.sql import func


class Role(Base):
    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
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

