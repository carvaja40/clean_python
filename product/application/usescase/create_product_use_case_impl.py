from product.application.usescase.create_product_use_case import CreateProductUseCase
from product.domain.model.product import Product
from product.infrastructure.persistence.product_repository import ProductRepository

"""
    Use case to representation the functionality the Products
"""


class CreateProductUseCaseImpl(CreateProductUseCase):
    """
        This Class has the responsibility the creation a product
    """

    def __init__(self, product_repository: ProductRepository) -> None:
        """
            Inicializer class
        """
        self.product_repository = product_repository

    def execute(self, product: Product) -> str:
        """
            Create a product
        """
        self.product_repository.save(product)
        return "execute Ok" + product.name
