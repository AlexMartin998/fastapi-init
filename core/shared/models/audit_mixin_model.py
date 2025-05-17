from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Column
from sqlalchemy import text


class AuditMixinModel(SQLModel):
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            nullable=False,
            server_default=text("timezone('utc'::text, now())")
        )
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            nullable=False,
            onupdate=lambda ctx: datetime.now(timezone.utc),
            server_default=text("timezone('utc'::text, now())")
        )
    )
