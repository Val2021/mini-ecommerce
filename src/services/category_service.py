from src.domain.category.model import Category
from src.services.category_dto import CategoryDTO
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

def create_category(category_dto:CategoryDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.category_repository.add(Category(name=category_dto.name))
    uow.commit()
