from abc import ABC, abstractmethod
from product.domain.model.product import Product
from typing import List


class ProductRepository(ABC):
    """
        Abstract base class for product repositories.

        Attributes:
            None

        Methods:
            save(product: Product) -> int:
                Abstract method to save a product.
                Args:
                    product (Product): The product object to be saved.
                Returns:
                    int: The unique identifier assigned to the saved product.

            get_by_id(product_id: int) -> Product:
                Abstract method to retrieve a product by its identifier.
                Args:
                    product_id (int): The identifier of the product to retrieve.
                Returns:
                    Product: The product object associated with the given identifier.

            get_products() -> List[Product]:
                Abstract method to retrieve a list of all products.
                Returns:
                    List[Product]: A list containing all products.

            update(product: Product) -> bool:
                Abstract method to update a product.
                Args:
                    product (Product): The product object to be updated.
                Returns:
                    bool: True if the update is successful, False otherwise.
        """
    @abstractmethod
    def save(self, product: Product) -> int:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass

    def get_products(self) -> List[Product]:
        pass

    def update(self, product: Product) -> bool:
        pass
