from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter

from src.products.models.category_model import Category

""" 
class AddressFilter(Filter):
    street: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    city__in: Optional[list[str]] = None
    custom_order_by: Optional[list[str]] = None
    custom_search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Address
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["street", "country", "city"]
"""

class CategoryFilter(Filter):
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

    # Búsquedas avanzadas por substring
    code__like:    Optional[str]  = None    # case-sensitive LIKE '%value%'
    code__ilike:   Optional[str]  = None    # case-insensitive LIKE '%value%'
    name__like:    Optional[str]  = None
    name__ilike:   Optional[str]  = None
    description__ilike: Optional[str] = None

    # order_by: Optional[list[str]] = None
    # page: Optional[int] = None
    # page_size: Optional[int] = None

    class Constants(Filter.Constants):
        model = Category
