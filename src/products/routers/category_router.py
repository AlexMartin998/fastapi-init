from fastapi import APIRouter, Query, status, Depends
from typing import List

from src.products.schemas.category_schema import CategoryRead, CategoryCreate, CategoryUpdate
from src.products.services.category_service import CategoryService
from src.products.dependencies.products_di import get_category_service

router = APIRouter(prefix="/categories", tags=["categories"])


# from fastapi_filter import FilterDepends
# from src.products.models.category_model import Category
# from sqlmodel import select
# from sqlmodel.ext.asyncio.session import AsyncSession
# from config.db import get_session


# @router.get("/", response_model=List[CategoryRead])
# async def list_categories(
#     category_filter: FilterDepends = FilterDepends(Category),
#     session: AsyncSession   = Depends(get_session),
# ):
#     query = category_filter.apply(select(Category))
#     result = await session.exec(query)
#     return result.all()



from fastapi_filter import FilterDepends
from src.products.models.category_model import Category
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from config.db import get_session
from src.products.filters.category_filter import CategoryFilter

@router.get("/", response_model=List[CategoryRead])
async def list_categories(
    category_filter: CategoryFilter = FilterDepends(CategoryFilter),
    session:        AsyncSession    = Depends(get_session),
):
    query  = category_filter.filter(select(Category))
    result = await session.execute(query)       # execute() existe aquí
    return result.scalars().all()               # scalars() extrae tus modelos

# @router.get("/", response_model=List[CategoryRead])
# async def list_categories(
#     offset: int = Query(0, ge=0),
#     limit: int = Query(100, le=200),
#     service: CategoryService = Depends(get_category_service),
# ):
#     return await service.find_all(offset, limit)




@router.get("/{category_id}", response_model=CategoryRead)
async def get_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service),
):
    return await service.find_one(category_id)


@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def create_category(
    dto: CategoryCreate,
    service: CategoryService = Depends(get_category_service),
):
    return await service.create(dto)


@router.patch("/{category_id}", response_model=CategoryRead)
async def update_category(
    category_id: int,
    dto: CategoryUpdate,
    service: CategoryService = Depends(get_category_service),
):
    return await service.update(category_id, dto)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service),
):
    await service.delete(category_id)
