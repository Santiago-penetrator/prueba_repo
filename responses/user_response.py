from pydantic import BaseModel

class response_create_user(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    lastname: str
    type: int 
    image: int  
    