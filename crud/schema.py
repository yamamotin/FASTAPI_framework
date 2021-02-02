from pydantic import BaseModel
from typing import Optional

#pydantic basemodel schema

class Cats(BaseModel):
    id: int
    breed: str
    locorigin: str
    bodytype: str
    coatlenght: int
    pattern: Optional[bool] = None