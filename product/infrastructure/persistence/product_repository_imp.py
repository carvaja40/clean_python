# infrastructure/persistence/ProductRepository.py

from product.domain.model.product import Product
from product.infrastructure.persistence.product_repository import ProductRepository
from product.infrastructure.entity.product_entity import ProductEntity
from sqlalchemy.exc import SQLAlchemyError
from typing import List
import logging


class ProductMapper:
    @staticmethod
    def from_entity(entity) -> Product:
       return Product(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            sku=entity.sku,
            order_timestamp=entity.order_timestamp
        )

    @staticmethod
    def from_entities(entities: List[ProductEntity]) -> List[Product]:
        return [ProductMapper.from_entity(entity) for entity in entities]


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
            # self.db_session_.refresh(product_entity)
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

    def get_products(self) -> List[Product]:
        logging.info("ProductRepositoryImp::start")
        list_products = self.db_session_.query(ProductEntity).all()
        return ProductMapper.from_entities(list_products)

    def update(self, product: Product) -> bool:
        try:
            logging.info("ProductRepositoryImp::update::start")
            product_entity = self.db_session_.query(ProductEntity).filter_by(id=product.id).first()

            if product_entity:

                product_entity.name = product.name
                product_entity.description = product.description
                product_entity.sku = product.sku
                product_entity.order_timestamp = product.order_timestamp
                self.db_session_.add(product_entity)

                logging.info("ProductRepositoryImp::update::end")
                return True
            else:
                logging.error(f"ProductRepositoryImp::update::error: Product with id {product.id} not found.")
                return False

        except SQLAlchemyError as e:
            logging.error("ProductRepositoryImp::update::error")
            logging.error(e)
            return False


