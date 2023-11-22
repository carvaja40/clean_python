from product.application.usescase.create_product_use_case import CreateProductUseCase
from product.application.usescase.create_product_use_case_impl import CreateProductUseCaseImpl
from product.infrastructure.persistence.product_repository import ProductRepository


class FactoryUsesCase:
    """
    Factory Uses Case
    """

    @staticmethod
    def create_product_use_case(product_repository: ProductRepository) -> CreateProductUseCase:
        """
        Method to create  Product Use Case Impl
        """
        return CreateProductUseCaseImpl(product_repository)
