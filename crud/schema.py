from datetime import datetime
from pydantic import BaseModel

#pydantic basemodel schema

class Cats(BaseModel):
    id: int
    breed: str
    loc_origin: str
    coat_lenght: int
    pattern: bool