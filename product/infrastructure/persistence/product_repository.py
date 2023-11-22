from abc import ABC, abstractmethod
from product.domain.model.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> int:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass
