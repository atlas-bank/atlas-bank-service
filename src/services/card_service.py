import logging
import os
from datetime import datetime
from http import HTTPStatus

from dtos.create_card_dto import CreateCardDTO
from exceptions.exceptions import InternalServerError
from services.api_request import ApiRequest
from services.api_response import api_response

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class CardService:
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

    def create_card(self, card: CreateCardDTO):
        card.userCPF = self.parse_cpf(card.userCPF)
        print(card.model_dump())
        response = self.request.post_request(endpoint="/card", data=card.model_dump())
        response["data"]["expirationDate"] = self.parse_expiration_date(response["data"]["expirationDate"])
        return api_response(
            status_code=HTTPStatus.CREATED,
            message=response["message"],
            data=response["data"],
        )

    def get_cards_by_cpf(self, cpf: str):
        response = self.request.get_request(endpoint=f"/cards/{cpf}")
        print(response)
        return api_response(
            status_code=HTTPStatus.OK,
            message=response["message"],
            data=response["data"],
        )
