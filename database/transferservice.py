from datetime import datetime

from database.models import Transfer, UserCard
from database import get_db


# private method
def _validate_card_db(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    check_card_from = _validate_card_db(card_from, db)
    check_card_to = _validate_card_db(card_to, db)

    if check_card_from and check_card_to:
        if check_card_from.balance >= amount:
            check_card_from.balance -= amount
            check_card_to.balance += amount

            new_transaction = Transfer(card_from_id=check_card_from.card_id, card_to_id=check_card_to.card_id,
                                       amount=amount, transaction_date=datetime.now())
            db.add(new_transaction)
            db.commit()

            return "Transfer is successful"

        else:
            return 'Not enough for transaction'
    return 'Card not found'


def get_card_transaction_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    return card_transaction


def cancel_transaction_db(card_from, card_to, amount, transfer_id):
    db = next(get_db())

    check_card_from = _validate_card_db(card_from, db)
    check_card_to = _validate_card_db(card_to, db)

    if check_card_from and check_card_to:
        if check_card_to.balance >= amount:
            check_card_from.balance += amount
            check_card_to.balance -= amount

            exact_transaction = db.query(Transfer).filter_by(transfer_id=transfer_id).first()
            exact_transaction.status = False
            db.commit()

            return "Transfer cancel is successful"

        else:
            return 'Not enough for transaction'

    return 'Card not found'