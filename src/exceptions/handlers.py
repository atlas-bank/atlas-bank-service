from http import HTTPStatus

from fastapi import Request

from exceptions.exceptions import UnauthorizedException, BadRequestException
from services.api_response import api_response


def register_exception_handlers(app):
    @app.exception_handler(UnauthorizedException)
    async def unauthorized_handler(request: Request, exc: UnauthorizedException):
        return api_response(message=str(exc), status_code=HTTPStatus.UNAUTHORIZED)

    @app.exception_handler(BadRequestException)
    async def bad_request_handler(request: Request, exc: BadRequestException):
        return api_response(message=str(exc), status_code=HTTPStatus.BAD_REQUEST)
