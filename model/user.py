from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(alias="Id")
    name: str = Field(alias="User Name")
    is_admin: bool = Field(alias="IsAdmin")
    
class Token(BaseModel):
    type: str
    access_token: str
    
class Payload(BaseModel):
    user_id: int
