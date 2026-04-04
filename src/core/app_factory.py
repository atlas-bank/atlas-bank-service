from fastapi import FastAPI, Depends
from fastapi.middleware import cors

from exceptions.handlers import register_exception_handlers
from services.api_key_validate import validate_api_key

#criação das configurações do FastApi
def create_app() -> FastAPI:
    app = FastAPI(
        title="Atlas API",
        version="1.0.0",
        dependencies=[Depends(validate_api_key)]
    )

    app.add_middleware(
        cors.CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    register_exception_handlers(app)

    return app