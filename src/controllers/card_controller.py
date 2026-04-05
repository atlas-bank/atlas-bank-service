from fastapi import APIRouter

from dtos.create_card_dto import CreateCardDTO
from services.card_service import CardService

router = APIRouter()

service = CardService()


@router.post("/card")
def create_card(card: CreateCardDTO):
    return service.create_card(card)


@router.get("/cards/{cpf}")
def get_cards_by_cpf(cpf: str):
    return service.get_cards_by_cpf(cpf)
