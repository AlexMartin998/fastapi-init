from typing import Optional
from uuid import UUID as UUIDType

from sqlmodel import SQLModel, Field

from src.products.models.category_model import CategoryBase


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int
    uuid: UUIDType

    class Config:
        orm_mode = True


class CategoryUpdate(SQLModel):
    code: Optional[str] = Field(None, max_length=20)
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=250)
    is_active: Optional[bool] = None
