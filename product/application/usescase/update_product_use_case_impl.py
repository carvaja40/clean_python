from product.application.interface.update_product_use_case import UpdateProductUseCase
from product.domain.model.product import Product
from product.application.repository.product_repository import ProductRepository


class UpdateProductUseCaseImpl(UpdateProductUseCase):
    """
        Concrete implementation of the UpdateProductUseCase interface.

        Attributes:
            repository_product (ProductRepository): The repository for managing products.

        Methods:
            __init__(repository_product: ProductRepository):
                Initializes the UpdateProductUseCaseImpl instance with the specified product repository.

            update(product: Product) -> bool:
                Updates a product using the provided information.

        """

    def __init__(self, repository_product: ProductRepository):
        """
                Initializes the UpdateProductUseCaseImpl instance.

                Args:
                    repository_product (ProductRepository): The repository for managing products.
                """
        self.repository_product = repository_product

    def update(self, product: Product) -> bool:
        """
        Updates a product using the provided information.

        Args:
            product (Product): The product object containing updated information.

        Returns:
            bool: True if the update is successful, False otherwise.
        """
        return self.repository_product.update(product)
