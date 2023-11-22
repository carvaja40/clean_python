# infrastructure/persistence/ProductRepository.py

from product.domain.model.product import Product
from product.infrastructure.persistence.product_repository import ProductRepository
from product.infrastructure.entity.product_entity import ProductEntity
from sqlalchemy.exc import SQLAlchemyError
import logging


class ProductRepositoryImp(ProductRepository):

    def __init__(self, db_session):
        self.db_session_ = db_session

    def save(self, product: Product) -> int:
        """
        """
        try:
            logging.info("ProductRepositoryImp::save::start")
            product_entity = ProductEntity(**product.__dict__)
            self.db_session_.add(product_entity)
            #self.db_session_.refresh(product_entity)
            logging.info("ProductRepositoryImp::save::end")
            return product_entity.id
        except SQLAlchemyError as e:
            logging.error("ProductRepositoryImp::save:error")
            logging.error(e)
            return -1

    def get_by_id(self, product_id: int) -> Product | None:
        product_entity = self.db_session_.query(ProductEntity).filter_by(id=product_id).first()
        if product_entity:
            return Product(**product_entity.__dict__)
        return None
