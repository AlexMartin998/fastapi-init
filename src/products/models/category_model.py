import uuid
from typing import Optional
from uuid import UUID as UUIDType
from sqlalchemy import UniqueConstraint, text, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import SQLModel, Field


from core.shared.models.audit_mixin_model import AuditMixinModel


class CategoryBase(SQLModel):
    code: str = Field(..., max_length=20, index=True)
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(default=None, max_length=250)
    is_active: bool = Field(default=True)


class Category(AuditMixinModel, CategoryBase, table=True):
    __table_args__ = (UniqueConstraint("code", name="uq_category_code"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: UUIDType = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            UUID(as_uuid=True),
            server_default=text("gen_random_uuid()"),
            nullable=False,
            unique=True,
            index=True,
        ),
    )
