from fastapi import APIRouter

from dtos.create_card_dto import CreateCardDTO
from services.card_service import CardService

router = APIRouter()

service = CardService()


@router.post("/card")
def create_card(card: CreateCardDTO):
    return service.create_card(card)
