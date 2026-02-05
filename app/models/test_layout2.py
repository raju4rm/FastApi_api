from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.db.database  import Base
from sqlalchemy.sql import func


class TestLayout2(Base):
    __tablename__ = "test_layout2"

    test_layout2_id = Column(Integer, primary_key=True, index=True)
    input_box = Column(String(255), nullable=False)
    select_box = Column(String(255), nullable=False)
    is_active = Column(String(255), nullable=True)
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

