from pydantic import BaseModel, EmailStr
from typing import Optional


class Create(BaseModel):
    input_box: str
    select_box: str   

