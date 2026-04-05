import os

import requests

from enums.methods import Methods
from exceptions.exceptions import BadRequestException, UnauthorizedException


class ApiRequest:

    def __init__(self, url: str):
        self.api_key = os.getenv("API_KEY_INTERNAL")
        self.url = url

    def __request(self, method: Methods, url: str, **kwargs):
        response = requests.request(
            method=method.value,
            url=url,
            headers={
                "x-api-key": self.api_key
            },

            **kwargs)

        return response

    def post_request(self, endpoint: str, data: dict = None) -> dict:
        response = self.__request(Methods.POST, self.url + endpoint, json=data)
        print(response.json())
        message = response.json()["message"]

        if response.status_code == 400:
            raise BadRequestException(message)
        if response.status_code == 401:
            raise UnauthorizedException(message)

        return response.json()
