from fastapi import APIRouter,status,Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from database import Session,engine
from schema import SignUpModel,LoginModel
from fastapi_jwt_auth import AuthJWT
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)

session = Session()

@auth_router.get("/")
def index():
    return "Hello, this is a home page of auth router"

# Singup Route
@auth_router.post("/signup",status_code=status.HTTP_201_CREATED,
                    response_description="The user has been created successfully")
async def signup(user:SignUpModel):
    print("<" + "--"*30 + '>')
    db_email  = session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
        # return {"message":"Email already exists"}

    db_username  = session.query(User).filter(User.username == user.username).first()

    if db_username is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
        # return {"message":"Username already exists"}
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_staff=user.is_staff if hasattr(user, 'is_staff') else False,
        is_active=user.is_active if hasattr(user, 'is_active') else False
    )

    session.add(new_user)
    session.commit()
    # Return the created user details
    return {
        "username": new_user.username,
        "email": new_user.email,
        "is_staff": new_user.is_staff,
        "is_active": new_user.is_active
    }

# Login Route
@auth_router.post('/login/')
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):
    db_user = session.query(User).filter(user.username == User.username).first()
    if db_user and check_password_hash(db_user.password,user.password):
        access_token = Authorize.create_access_token(subject=db_user.username)
        refresh_token = Authorize.create_refresh_token(subject=db_user.username)

        response = {
            "access_token" : access_token,
            "refresh_token" : refresh_token
        }
        return JSONResponse(content=response,status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid username or password!")