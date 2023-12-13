
import uvicorn
from os import getenv
from fastapi import FastAPI
from routers import products, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origin = [
    # 'http://localhost:3000'
    '*'
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origin,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

# routers
app.include_router(products.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
