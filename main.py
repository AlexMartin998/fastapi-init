# src/main.py
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from config.db import async_engine  # tu AsyncEngine
from src.products.routers.category_router import router as category_router
# from dependencies.category import get_category_service
# from errors import register_all_errors
# from middleware import register_middleware

version = "v1"
version_prefix = f"/api/{version}"

description = """
API de Categorías:
- Crear, listar, actualizar y eliminar categorías
- Relaciones jerárquicas padre/hijo
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: inicializa tablas en dev/CI (en prod usa Alembic)
    async with async_engine.begin() as conn:
        await conn.run_sync(lambda conn: None)  # o tu función init_db
    yield
    # Shutdown: cierra el engine
    await async_engine.dispose()

app = FastAPI(
    title="Mi API de Categorías",
    version=version,
    description=description,
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
    lifespan=lifespan
)

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from core.shared.exceptions.custom_exception import CustomException
from core.shared.exceptions.not_found_exception import NotFoundException
@app.exception_handler(CustomException)
async def not_found_exception_handler(request: Request, exc: CustomException):
    if isinstance(exc, NotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.message}  # o {"message": exc.message}
        )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error"}
    )
    

# Errores y middleware
# register_all_errors(app)
# register_middleware(app)

# Routers
app.include_router(
    category_router,
    prefix=f"{version_prefix}/categories",
    tags=["categories"]
)

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # deshabilitar en producción
    )
