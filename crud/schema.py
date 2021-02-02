from datetime import datetime
from pydantic import BaseModel
from typing import Optional

#pydantic basemodel schema

class Cats(BaseModel):
    id: int
    breed: str
    loc_origin: str
    body_type: str
    coat_lenght: int
    pattern: Optional[bool] = None