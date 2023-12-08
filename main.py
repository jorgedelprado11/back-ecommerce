from fastapi import FastAPI
from routers import products
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# routers
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)