from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username: str
    email: str
    password: str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode =True
        schema_extra = {
            'example':{
                'username':"Ramlal12",
                'email':"ramlal12@gmail.com",
                'password':"ramlal12",
                'is_staff':True,
                'is_active':False
            }
        }
