import logging
import os
from http import HTTPStatus

from dtos.create_card_dto import CreateCardDTO
from services.api_response import api_response

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class CardService:
    def __init__(self):
        tsp_url = os.getenv("")

    def create_card(self, card: CreateCardDTO):
        print(card.model_dump())
        return api_response(
            status_code=HTTPStatus.NOT_IMPLEMENTED,
            message="Not implemented",
            data=card.model_dump(),
        )
