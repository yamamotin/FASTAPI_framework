from pydantic import BaseModel, Field
from typing import Optional

#pydantic basemodel schema
class Cats(BaseModel):
    id: int
    breed: str
    location_of_origin: str
    coat_length: str
    body_type: int
    pattern: Optional[bool] = False

class CatsRegister(BaseModel):
    breed: str = Field(..., example="begal cat")
    location_of_origin: str = Field(..., example="begal cat")
    coat_length: str = Field(..., example="begal cat")
    body_type: int = Field(..., example="10")
    pattern: Optional[bool] = Field(..., example="False")

class CatsUpdate(BaseModel):
    id : str = Field(..., example="Enter your id")
    breed: str = Field(..., example="begal cat")
    location_of_origin: str = Field(..., example="begal cat")
    coat_length: str = Field(..., example="begal cat")
    body_type: int = Field(..., example="10")
    pattern: Optional[bool] = Field(..., example="False")