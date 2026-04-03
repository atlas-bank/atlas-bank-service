from http import HTTPStatus

from fastapi import FastAPI, Depends, Request

from exceptions.handlers import register_exception_handlers
from services.api_key_validate import validate_api_key
from services.api_response import api_response

app = FastAPI(
    title="Atlas API",
    version="1.0.0",
    dependencies=[Depends(validate_api_key)]
)

register_exception_handlers(app)


@app.get("/")
def health(request: Request):
    return api_response(
        status_code=HTTPStatus.OK,
        message="OK",
        data=dict(request.headers)
    )
