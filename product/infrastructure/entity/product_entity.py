from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductEntity(Base):
    __tablename__ = 'products_2'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    sku = Column(String, index=True)
    order_timestamp = Column(String)
