from typing import Generic, List, TypeVar
from fastapi import HTTPException, status
from sqlmodel import SQLModel

from core.shared.exceptions.not_found_exception import NotFoundException

ModelType = TypeVar("ModelType", bound=SQLModel)


class GenericService(Generic[ModelType]):
    """Lógica de negocio genérica con validaciones comunes."""

    def __init__(self, repository):
        self.repo = repository  # instancia de GenericRepository

    async def find_all(self, offset: int, limit: int) -> List[ModelType]:
        return await self.repo.find_all(offset, limit)

    async def find_one(self, obj_id: int) -> ModelType:
        obj = await self.repo.find_one(obj_id)
        if not obj:
            raise NotFoundException(f"Object with id {obj_id} not found")
        return obj

    async def create(self, create_dto) -> ModelType:
        instance = self.repo.model(**create_dto.dict())
        created = await self.repo.create(instance)
        await self.repo.commit()
        return created

    async def update(self, obj_id: int, update_dto) -> ModelType:
        obj = await self.find_one(obj_id)
        for field, value in update_dto.dict(exclude_unset=True).items():
            setattr(obj, field, value)
        updated = await self.repo.update(obj)
        await self.repo.commit()
        return updated

    async def delete(self, obj_id: int) -> None:
        obj = await self.find_one(obj_id)
        await self.repo.delete(obj)
        await self.repo.commit()
