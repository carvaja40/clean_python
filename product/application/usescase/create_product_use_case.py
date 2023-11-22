from abc import ABC, abstractmethod
from product.domain.model.product import Product


class CreateProductUseCase(ABC):

    @abstractmethod
    def execute(self, product: Product) -> str:
        """
        """
        pass
