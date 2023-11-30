from abc import ABC, abstractmethod
from product.domain.model.product import Product


class ListProductUseCase(ABC):

    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass
