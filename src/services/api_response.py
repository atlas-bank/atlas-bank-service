from http import HTTPStatus

from fastapi.responses import JSONResponse


def api_response(status_code: HTTPStatus, message: str, data: dict = None):
    content = {
        "message": message
    }

    if data:
        content["data"] = data

    return JSONResponse(
        status_code=status_code,
        content=content
    )
