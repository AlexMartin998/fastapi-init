# from typing import List

from core.shared.services.generic_service import GenericService
from src.products.models.category_model import Category
from src.products.repositories.category_repository import CategoryRepository
# from schemas.category_schema import CategoryCreate, CategoryUpdate


class CategoryService(GenericService[Category]):

    def __init__(self, repo: CategoryRepository):
        super().__init__(repo)
