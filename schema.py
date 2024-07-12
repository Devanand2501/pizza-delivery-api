from pydantic import BaseModel,Field
from typing import Optional

# SignUp model
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

# To generate token 
'''
import secrets 
secrets.token_hex()
'''
# Setting model
class Settings(BaseModel):
    # authjwt_secret_key:str = Field(default='8615264fbd0f0b30da7eb5fe12e022b3845ae0a64b0106cbc787374a1fbfc56c')
    authjwt_secret_key:str = '8615264fbd0f0b30da7eb5fe12e022b3845ae0a64b0106cbc787374a1fbfc56c'

# Login Model
class LoginModel(BaseModel):
    username: str
    password: str

# Order Model
class OrderModel(BaseModel):
    id:Optional[int]
    quantity: int
    order_status : Optional[str] = "pending"
    pizza_size : Optional[str] = "small"

    class Config:
        from_attributes =True
        json_schema_extra = {
            'example':{
                'quantity':2,
                'pizza_size':"large",
                'order_status':"pending",
            }
        }

class OrderStatusModel(BaseModel):
    order_status: Optional[str]="pending"
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            'example':{
                'order_status':"proceed"
            }
        }