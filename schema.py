from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    username: str
    email: str
    password: str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        from_attributes =True
        json_schema_extra = {
            'example':{
                'username':"Ramlal12",
                'email':"ramlal12@gmail.com",
                'password':"ramlal12",
                'is_staff':True,
                'is_active':False
            }
        }
