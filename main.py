from fastapi import Depends, FastAPI
from product.infrastructure.controller import product_controller

app = FastAPI()
app.include_router(product_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
