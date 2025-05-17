from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from .settings import settings
import src.products.models.category_model


print('---------> db.py', settings.database_url)

# 1. Engine asíncrono nativo
async_engine: AsyncEngine = create_async_engine(
    settings.database_url,          # e.g. "postgresql+asyncpg://user:pass@host/db"
    echo=False,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)


# 2. Fábrica de sesiones asíncronas
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)


# 3. Inicialización de tablas (solo en desarrollo/integración continua)
async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# 4. Dependencia de FastAPI


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
