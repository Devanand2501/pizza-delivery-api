from fastapi import APIRouter,Depends,status
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from database  import Session
from models import User,Order
from schema import OrderModel

order_router = APIRouter(
    prefix = "/orders",
    tags = ["orders"]
)

# Order Home Page
@order_router.get("/")
def index(Authorizer:AuthJWT = Depends()):
    try:
        Authorizer.jwt_required()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail={"access":"Invalid Token"})
    return "Hello, this is a home page of order router"

# Put order
@order_router.post("/put_order/",status_code=status.HTTP_201_CREATED)
def put_order(order:OrderModel,Authorizer:AuthJWT=Depends()):
    try:
        Authorizer.jwt_required()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail={"access":"Invalid Token"})
    
    session = Session()
    # Help to fetch current user using access token
    current_user = Authorizer.get_jwt_subject()

    user = session.query(User).filter(current_user == User.username).first()

    if user is None:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User doesn't exist!")
    else:
        new_order = Order(
            user_id = user.id,
            quantity = order.quantity,
            pizza_size = order.pizza_size,
            order_status = order.order_status
        )
        session.add(new_order)
        session.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content={"message":"Order has been placed successfully!"})

# Get all orders
@order_router.get("/all_orders/")
def put_order(Authorizer:AuthJWT=Depends()):
    try:
        Authorizer.jwt_required()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail={"access":"Invalid Token"})
    
    session = Session()
    # Help to fetch current user using access token
    current_user = Authorizer.get_jwt_subject()
    user = session.query(User).filter(current_user == User.username).first()
    if user is None:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User doesn't exist!")
    
    if user.is_staff:
        orders = session.query(Order).all()
        print(orders)
        return jsonable_encoder(orders)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="You don't have access!")

