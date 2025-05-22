from fastapi import FastAPI, APIRouter

from views.ExpenseViews import expenses_router
from views.UserViews import user_router

app = FastAPI()

router = APIRouter()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(prefix="/api", router=router)
app.include_router(user_router, prefix="/api")

app.include_router(expenses_router, prefix="/api")


