from sqlmodel.ext.asyncio.session import AsyncSession

from src.products.models.category_model import Category
from core.shared.repositories.generic_repository import GenericRepository


class CategoryRepository(GenericRepository[Category]):

    def __init__(self, session: AsyncSession):
        super().__init__(Category, session)
