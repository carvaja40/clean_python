from product.application.interface.create_product_use_case import CreateProductUseCase
from product.application.usescase.create_product_use_case_impl import CreateProductUseCaseImpl
from product.application.interface.list_product_use_case import ListProductUseCase
from product.application.usescase.list_product_use_case_impl import ListProductImplUseCase
from product.application.interface.update_product_use_case import UpdateProductUseCase
from product.application.usescase.update_product_use_case_impl import UpdateProductUseCaseImpl
from product.application.repository.product_repository import ProductRepository


class FactoryUsesCase:
    """
    Factory Uses Case
    """

    @staticmethod
    def create_product_use_case(product_repository: ProductRepository) -> CreateProductUseCase:
        """
        Method to create Product Use Case Impl
        """
        return CreateProductUseCaseImpl(product_repository)

    @staticmethod
    def list_product_use_case(product_repository: ProductRepository) -> ListProductUseCase:
        """
        Method to get a list the products.
        """
        return ListProductImplUseCase(product_repository)

    @staticmethod
    def update_product_use_case(product_repository: ProductRepository) -> UpdateProductUseCase:
        return UpdateProductUseCaseImpl(product_repository)



