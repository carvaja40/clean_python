import logging
from fastapi import APIRouter, Depends, HTTPException
from product.application.factory.factory_uses_case import FactoryUsesCase
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
async def create(product: Product, uow: UnitOfWork = Depends(get_uow)):
    try:
        logging.info("post:method:create::start")
        product_repository = get_product_repository(uow.session)
        create_product_business_case = FactoryUsesCase.create_product_use_case(product_repository)
        create_product_business_case.execute(product)
        uow.commit()
        logging.info("post:method:create::end")
        return {"message": "Product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        print("finally")


@router.put("/")
async def update(product: Product, uow: UnitOfWork = Depends(get_uow)):
    try:
        logging.info("put::method::update::start")
        product_repository = get_product_repository(uow.session)
        update_product_use_case = FactoryUsesCase.update_product_use_case(product_repository)
        update_product_use_case.update(product)
        uow.commit()
        logging.info("put::method::update::end")
        return {"message": "Update created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        logging.info("put::method::update::end::finally")


@router.get("/")
async def get_products(uow: UnitOfWork = Depends(get_uow)):
    logging.info("get:method:get_products::start")
    product_repository = get_product_repository(uow.session)
    list_product_business_case = FactoryUsesCase.list_product_use_case(product_repository)
    products = list_product_business_case.get_products()
    logging.info("get:method:get_products::end")
    return {"product": products}


@router.get("/get_product/{product_id}", response_model=Product)
async def get_products_id(product_id: int, uow: UnitOfWork = Depends(get_uow)):
    try:
        logging.info("update::start")
        product_repository = get_product_repository(uow.session)
        create_product_business_case = FactoryUsesCase.list_product_use_case(product_repository)
        product_ = create_product_business_case.get_product_by_id(product_id)
        return product_
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        print("finally")
