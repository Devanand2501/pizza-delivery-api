from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException
from database import Session,engine
from schema import SignUpModel
from models import User
from werkzeug.security import generate_password_hash

auth_router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)

session = Session(bind=engine)

@auth_router.get("/")
def index():
    return "Hello, this is a home page of auth router"

@auth_router.post("/signup",status_code=status.HTTP_201_CREATED,
                    response_description="The user has been created successfully")
async def signup(user:SignUpModel):
    print("hello")
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