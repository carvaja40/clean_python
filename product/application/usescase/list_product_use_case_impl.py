from product.application.usescase.list_product_use_case import ListProductUseCase
from product.domain.model.product import Product
from product.infrastructure.persistence.product_repository import ProductRepository
from typing import List


class ListProductImplUseCase(ListProductUseCase):

    def __init__(self, product_repository: ProductRepository) -> None:
        """
            Inicializer class
        """
        self.product_repository = product_repository

    def get_products(self) -> List[Product]:
        """
        Method to get a List Products
        """
        list_products: List[Product] = self.product_repository.get_products()
        return list_products

    def get_product_by_id(self, product_id: int) -> Product:
        product_: Product = self.product_repository.get_by_id(product_id)
        return product_
