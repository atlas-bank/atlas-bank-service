from fastapi import FastAPI, Depends
from fastapi.middleware import cors

from controllers import account_controller
from exceptions.handlers import register_exception_handlers
from services.api_key_validate import validate_api_key
from controllers.card_controller import router as card_controller
from controllers.account_controller import router as account_controller

#criação das configurações do FastApi
def create_app() -> FastAPI:
    app = FastAPI(
        title="Atlas API",
        version="1.0.0",
        dependencies=[Depends(validate_api_key)]
    )

    app.include_router(card_controller)
    app.include_router(account_controller)

    app.add_middleware(
        cors.CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    register_exception_handlers(app)

    return app