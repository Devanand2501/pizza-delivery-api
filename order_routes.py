from fastapi import APIRouter

order_router = APIRouter(
    prefix = "/orders",
    tags = ["orders"]
)

@order_router.get("/")
def index():
    return "Hello, this is a home page of order router"