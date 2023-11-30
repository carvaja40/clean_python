from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from product.infrastructure.controller import product_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(product_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
