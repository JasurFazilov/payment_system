from fastapi import APIRouter, Depends
import requests

from redis_service import redis_db


currency_router = APIRouter(prefix='/currency', tags=['Currency'])


def _check_currency_rates_redis():
    usd = redis_db.get('USD')
    rub = redis_db.get('RUB')
    eur = redis_db.get('EUR')
    jpy = redis_db.get('JPY')
    cny = redis_db.get('CNY')

    if usd and rub and eur and jpy and cny:
        return {'USD': usd.decode(), 'RUB': rub.decode(), 'EUR': eur.decode(), 'JPY': jpy.decode(), 'CNY': cny.decode()}

    return False


@currency_router.post('/get-rates')
async def get_currency_rates(redis_checker=Depends(_check_currency_rates_redis)):
    if redis_checker:
        print('from redis')
        return {'status': 1, 'rates': redis_checker}


    cb_url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
    response = requests.get(cb_url).json()

    usd_eur_rub_jpy_cny = [i for i in response if i['Ccy'] in ['EUR', 'RUB', 'USD', 'JPY', 'CNY']]

    redis_db.set('USD', usd_eur_rub_jpy_cny[0]['Rate'], 5)
    redis_db.set('EUR', usd_eur_rub_jpy_cny[1]['Rate'], 5)
    redis_db.set('RUB', usd_eur_rub_jpy_cny[2]['Rate'], 5)
    redis_db.set('JPY', usd_eur_rub_jpy_cny[3]['Rate'], 5)
    redis_db.set('CNY', usd_eur_rub_jpy_cny[4]['Rate'], 5)
    print('not redis')


    return {'status': 1, 'rates': usd_eur_rub_jpy_cny}

