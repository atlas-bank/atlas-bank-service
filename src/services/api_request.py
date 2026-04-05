import os

import requests

from enums.methods import Methods


class ApiRequest:

    def __init__(self):
        self.api_key = os.getenv("API_KEY_INTERNAL")

    def __request(self, method: Methods, url: str, **kwargs):
        response = requests.request(
            method=method.value,
            url=url,
            headers={
                "x-api-key": self.api_key
            },

            **kwargs)

        return response

    def post_request(self, url: str, data: dict = None):
        return self.__request(Methods.POST, url, json=data)
