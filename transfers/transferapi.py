from fastapi import APIRouter
from datetime import datetime
from database.transferservice import create_transaction_db, cancel_transaction_db, get_card_transaction_db
from transfers import CancelTransferModel, CardTransferModel

transaction_router = APIRouter(prefix='/transaction', tags=['Transaction menu'])

@transaction_router.post('/create')
async def add_new_transaction(data: CardTransferModel):
    transaction_data = data.model_dump()
    result = create_transaction_db(**transaction_data)

    return {'status': 1, 'message': result}


@transaction_router.post('/cancel-transaction')
async def cancel_transaction(data: CancelTransferModel):
    cancel_data = data.model_dump()
    result = cancel_transaction_db(**cancel_data)

    return {'status': 1, 'message': result}


@transaction_router.get('/monitoring')
async def get_card_monitoring(card_id: int):
    result = get_card_transaction_db(card_from_id=card_id)

    return {'status': 1, 'message': result}

