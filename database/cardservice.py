from datetime import datetime

from database import get_db
from database.models import UserCard


def add_card_db(user_id, card_number, balance, exp_date, cvv):
    db = next(get_db())

    new_card = UserCard(user_id=user_id, card_number=card_number, balance=balance,
                        exp_date=exp_date, cvv=cvv)

    db.add(new_card)
    db.commit()

    return "New card added"


def delete_exact_card_db(card_id):
    db = next(get_db())

    exact_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if exact_card:
        db.delete(exact_card)
        db.commit()

        return 'Card deleted'

    return 'Card not found'


def edit_card_design_db(card_id, design_path):
    db = next(get_db())

    exact_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if exact_card:
        exact_card.card_design = design_path
        db.commit()

        return 'Design updated'

    return 'Card not found'


def get_exact_user_cards_db(user_id):
    db = next(get_db())

    exact_user_cards = db.query(UserCard).filter_by(user_id=user_id).all()

    return exact_user_cards


def get_exact_card_db(user_id, card_id):
    db = next(get_db())

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id).first()

    return exact_user_card


def check_card_info_db(card_number):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(card_number=card_number).first()

    return checker

