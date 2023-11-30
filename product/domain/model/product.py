# product/domain/model/Product.py
from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    sku: str
    order_timestamp: str
