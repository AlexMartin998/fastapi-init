# FASTAPI

Install deps:

```sh
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv pydantic-settings
pip install asyncpg 


pip freeze > requirements.txt
```



Dir tree:

```sh
project_root/
└── src/
    ├── database/
    │   ├── engine.py
    │   └── session.py
    ├── core/                      # Código compartido (config, excepciones, utilidades)
    │   ├── config.py
    │   └── exceptions.py
    ├── features/
    │   └── products/
    │       ├── __init__.py
    │       ├── models/
    │       │   ├── base.py         # DeclarativeBase si necesitas local
    │       │   ├── product.py
    │       │   └── category.py
    │       ├── schemas/
    │       │   ├── product_in.py
    │       │   ├── product_out.py
    │       │   └── category_out.py
    │       ├── repositories/
    │       │   ├── base_repository.py
    │       │   └── product_repository.py
    │       ├── services/
    │       │   ├── base_service.py
    │       │   └── product_service.py
    │       ├── api/
    │       │   ├── deps.py
    │       │   └── router.py
    │       └── filters/
    │           └── product_filter.py
    ├── main.py
    └── requirements.txt
```