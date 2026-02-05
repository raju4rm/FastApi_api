from sqlalchemy import Enum
from app.models.enums import StatusEnum

status_enum = Enum(
    StatusEnum,
    name="statusenum",     # PostgreSQL enum name
    create_type=False      # ⭐ CRITICAL
)
