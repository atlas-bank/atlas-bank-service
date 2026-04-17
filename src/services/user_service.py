import logging
import os
from datetime import datetime
from http import HTTPStatus

from exceptions.exceptions import InternalServerError
from services.api_request import ApiRequest
from services.api_response import api_response
from dtos.create_user_dto import CreateUserDTO
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class UserService:
    def __init__(self):
        tsp_url = os.getenv("TSP_URL")
        if not tsp_url:
            raise InternalServerError("TSP_URL not set")
        self.request = ApiRequest(tsp_url)

    @staticmethod
    def parse_expiration_date(expiration_date):
        date_obj = datetime.strptime(expiration_date, "%Y-%m-%d")

        return date_obj.strftime("%m/%y")

    @staticmethod
    def parse_cpf(cpf: str):
        return cpf.replace(".", "").replace("-", "")

    def create_user(self, user: CreateUserDTO):
        user.cpf = self.parse_cpf(user.cpf)
        print(user.model_dump())
        response = self.request.post_request(endpoint="/user", data=user.model_dump())
        response["data"]["expirationDate"] = self.parse_expiration_date(response["data"]["expirationDate"])
        return api_response(
            status_code=HTTPStatus.CREATED,
            message=response["message"],
            data=response["data"],
        )

    # def get_cards_by_cpf(self, cpf: str):
    #     response = self.request.get_request(endpoint=f"/cards/{cpf}")
    #     print(response)
    #
    #     for card in response["data"]:
    #         card["expirationDate"] = self.parse_expiration_date(card["expirationDate"])
    #
    #     return api_response(
    #         status_code=HTTPStatus.OK,
    #         message=response["message"],
    #         data=response["data"],
    #     )
