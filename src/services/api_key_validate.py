import os

from fastapi import Header

from exceptions.exceptions import UnauthorizedException


def validate_api_key(x_api_key: str = Header(None)):
    api_key_internal = os.getenv("API_KEY_INTERNAL")

    if not api_key_internal:
        raise UnauthorizedException("API_KEY_INTERNAL not configured")

    if not x_api_key:
        raise UnauthorizedException("x-api-key header is required")

    if x_api_key != api_key_internal:
        print(f"{api_key_internal} != {x_api_key}")
        raise UnauthorizedException("Invalid API Key")