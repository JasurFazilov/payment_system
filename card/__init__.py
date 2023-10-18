from pydantic import BaseModel


class CardAddModel(BaseModel):
    user_id: int
    card_number: int
    balance: float
    exp_date: int
    cvv: int

class EditCardModel(BaseModel):
    card_id: int
    design_path: str
