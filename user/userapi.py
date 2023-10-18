from fastapi import APIRouter
from datetime import datetime

from database.userservice import user_reg_db, edit_user_info_db, delete_exact_user_db, get_exact_user_info_db, \
    check_user_info_db
from user import UserRegisterModel, EditUserModel

user_router = APIRouter(prefix='/user', tags=['User data'])


@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    new_user_data = data.model_dump()
    checker = check_user_info_db(data.email)

    if not checker:
        result = user_reg_db(reg_date=datetime.now(), **new_user_data)

        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Email already used'}


@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_info_db(user_id)

    return {'status': 1 if result else 0, 'message': result}


@user_router.put('/edit-data')
async def edit_user(data: EditUserModel):
    change_data = data.model_dump()

    result = edit_user_info_db(**change_data)

    return {'status': 1, 'message': result}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_exact_user_db(user_id)

    return {'status': 1, 'message': result}