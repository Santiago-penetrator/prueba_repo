from pydantic import BaseModel,constr,validator
from typing import Optional

class UserM(BaseModel):
    id: int = Optional[int]
    email : str
    phone : str 
    name : str
    lastname : str
    type : int 
    image : str
    @validator("email")
    def email_especific_domain(cls,v):
        if"@kiritek.com" not in v:
            raise ValueError("Email must be from kiritek.com")
        return 
    
class UserU(UserM):
    id : int 

class UserC(UserM):
    password : str