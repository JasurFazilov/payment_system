from pydantic import BaseModel


class CardTransferModel(BaseModel):
    card_from: int
    card_to: int
    amount: int


class CancelTransferModel(BaseModel):
    transfer_id: int