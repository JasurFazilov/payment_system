from datetime import datetime

from database.models import User
from database import get_db


# Registration
def user_reg_db(name, surname, email, phone_number, city, password, reg_date):
    db = next(get_db())

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number, city=city, password=password, reg_date=reg_date)

    db.add(new_user)
    db.commit()


# User info

def get_exact_user_info_db(user_id):
    db = next(get_db())

    exact_user_info = db.query(User).filter_by(user_id=user_id).first()

    return exact_user_info


# checker (email)

def check_user_info_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    return checker


# edit info

def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_info == 'city':
            exact_user.city = new_info

        elif edit_info == 'email':
            exact_user.email = new_info

        elif edit_info == 'password':
            exact_user.password = new_info

        elif edit_info == 'name':
            exact_user.name = new_info

        elif edit_info == 'surname':
            exact_user.surname = new_info

        elif edit_info == 'phone_number':
            exact_user.phone_number = new_info

        db.commit()

        return 'Changes applied successfully'

    return 'User not found'

# Delete user

def delete_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()

        return 'User deleted'

    return 'User not found'