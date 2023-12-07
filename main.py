from fastapi import FastAPI
from routers import products
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# routers
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
