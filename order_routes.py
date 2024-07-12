from fastapi import APIRouter,Depends,status
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from database  import Session
from models import User,Order
from schema import OrderModel,OrderStatusModel

order_router = APIRouter(
    prefix = "/orders",
    tags = ["orders"]
)

# Order Home Page
@order_router.get("/")
async def index(Authorizer:AuthJWT = Depends()):
    try:
        Authorizer.jwt_required()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail={"access":"Invalid Token"})
    return "Hello, this is a home page of order router"

# Put order
@order_router.post("/put_order/",status_code=status.HTTP_201_CREATED)
async def put_order(order:OrderModel,Authorizer:AuthJWT=Depends()):
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
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
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
async def put_order(Authorizer:AuthJWT=Depends()):
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
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User doesn't exist!")
    
    if user.is_staff:
        orders = session.query(Order).all()
        print(orders)
        return jsonable_encoder(orders)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="You don't have access!")

# Retrieve a single order
@order_router.get("/order/{order_id}/")
async def get_order(order_id:int,Authorizer:AuthJWT = Depends()):
    try:
        Authorizer.jwt_required()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Token!")
    session = Session()
    current_user = Authorizer.get_jwt_subject()
    user = session.query(User).filter(User.username == current_user).first()
    if user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User doesn't exist!")
    order = session.query(Order).filter(Order.id == order_id).first()
    if order is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Order doesn't exist!")
    return jsonable_encoder(order)

# Update Order status 
@order_router.patch("/{order_id}/status")
async def update_order_status(order_id:int,
                                order:OrderStatusModel,
                                Authorizer:AuthJWT=Depends()):
    try:
        Authorizer.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Token!")
    session = Session ()
    current_user = Authorizer.get_jwt_subject()

    user = session.query(User).filter(current_user == User.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User doesn't exist!"
        )
    
    if not user.is_staff:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You don't have access!"
        )
    
    order_to_update = session.query(Order).filter(order_id == Order.id).first()
    if order_to_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order doesn't exist!"
        )
    
    order_to_update.order_status = order.order_status
    session.commit()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content="Order status updated successfully!"
    )
