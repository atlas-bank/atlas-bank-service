import os

from fastapi import Header

from exceptions.exceptions import UnauthorizedException

api_key_internal = os.getenv("API_KEY_INTERNAL")

def validate_api_key(x_api_key: str = Header(None)):
    if not api_key_internal:
        raise UnauthorizedException("API_KEY_INTERNAL not configured")

    if not x_api_key:
        raise UnauthorizedException("x-api-key header is required")

    if x_api_key != api_key_internal:
        raise UnauthorizedException("Invalid API Key")