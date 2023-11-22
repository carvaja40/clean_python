# product/domain/model/Product.py
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    sku: str
    order_timestamp: str
