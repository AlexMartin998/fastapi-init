from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from config.db import get_session
from src.products.repositories.category_repository import CategoryRepository
from src.products.services.category_service import CategoryService


async def get_category_repo(
    session: AsyncSession = Depends(get_session)
) -> CategoryRepository:
    return CategoryRepository(session)


async def get_category_service(
    repo: CategoryRepository = Depends(get_category_repo)
) -> CategoryService:
    return CategoryService(repo)
