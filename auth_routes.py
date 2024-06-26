from fastapi import APIRouter

auth_router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)

@auth_router.get("/")
def index():
    return "Hello, this is a home page of auth router"