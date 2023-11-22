from product.infrastructure.persistence.product_repository import ProductRepository
from product.infrastructure.persistence.product_repository_imp import ProductRepositoryImp


def get_product_repository(db_session: object) -> ProductRepository:
    return ProductRepositoryImp(db_session)

    