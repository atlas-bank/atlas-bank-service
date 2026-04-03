from http import HTTPStatus

from fastapi import Request

from core.app_factory import create_app
from services.api_response import api_response

app = create_app()

@app.get("/")
def health(request: Request):
    return api_response(
        status_code=HTTPStatus.OK,
        message="OK",
        data=dict(request.headers)
    )
