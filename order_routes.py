from fastapi import APIRouter,Depends,status
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

order_router = APIRouter(
    prefix = "/orders",
    tags = ["orders"]
)

@order_router.get("/")
def index(Authorizer:AuthJWT = Depends()):
    try:
        Authorizer.jwt_required()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail={"access":"Invalid Token"})
    return "Hello, this is a home page of order router"