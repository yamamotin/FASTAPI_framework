from pydantic import BaseModel, Field
from typing import Optional

#pydantic basemodel schema
class Cats(BaseModel):
    id: int
    breed: str
    location_of_origin: str
    coat_length: str
    body_type: str
    pattern: Optional[bool] = False

class CatsRegister(BaseModel):
    breed: str = Field(..., example="begal cat")
    location_of_origin: str = Field(..., example="begal cat")
    coat_length: str = Field(..., example="1")
    body_type: str = Field(..., example="Pequeno")
    pattern: Optional[bool] = Field(..., example="False")
