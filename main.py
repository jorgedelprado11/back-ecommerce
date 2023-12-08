
import uvicorn
from os import getenv
from fastapi import FastAPI
from routers import products


app = FastAPI()

# routers
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=True)
