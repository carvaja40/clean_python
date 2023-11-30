from abc import ABC, abstractmethod

from product.domain.model.product import Product


class UpdateProductUseCase(ABC):

    @abstractmethod
    def update(self, product: Product):
        pass
