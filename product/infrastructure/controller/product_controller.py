import logging

from fastapi import APIRouter, Depends, HTTPException

from product.application.usescase.factory_uses_case import FactoryUsesCase
from product.domain.model.product import Product
from product.infrastructure.persistence.factory_repository import get_product_repository
from product.infrastructure.persistence.unit_of_work import UnitOfWork

logging.basicConfig(level=logging.DEBUG)

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


def get_uow():
    with UnitOfWork() as uow:
        yield uow


@router.post("/")
async def root(product: Product, uow: UnitOfWork = Depends(get_uow)):
    try:
        uow.commit()
        product_repository = get_product_repository(uow.session)
        create_product_business_case = FactoryUsesCase.create_product_use_case(product_repository)
        create_product_business_case.execute(product)
        uow.commit()
        return {"message": "Product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        print("finally")
