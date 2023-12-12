
import uvicorn
from os import getenv
from fastapi import FastAPI
from routers import products,users


app = FastAPI()

# routers
app.include_router(products.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


