from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.customer_schema import CreateCustomerSchema
from src.services.customer_dto import CustomerDTO
from src.services.customer_service import create_customer
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateCustomerSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = CustomerDTO(**schema.dict())
  
  product = create_customer(dto, uow=uow)

  return product