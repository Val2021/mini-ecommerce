from fastapi import APIRouter
from src.presentation.fastapi.routes.product_router import router as product_router
from src.presentation.fastapi.routes.category_router import router as category_router
from src.presentation.fastapi.routes.supplier_router import router as supplier_router
from src.presentation.fastapi.routes.customer_router import router as customer_router
from src.presentation.fastapi.routes.address_router import router as address_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(category_router, prefix='/categories', tags=['categories'])
router.include_router(supplier_router, prefix='/supplier', tags=['suppliers'])
router.include_router(customer_router, prefix='/customers', tags=['customers'])
router.include_router(address_router, prefix='/address', tags=['addresses'])
