from fastapi import FastAPI
from starlette.templating import Jinja2Templates

from user.userapi import user_router

from card.cardapi import card_router

from transfers.transferapi import transaction_router

from currency.currencyapi import currency_router

from database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')

# for html of the page
template = Jinja2Templates(directory='templates')
from html_example.html_show import html_router
app.include_router(html_router)

app.include_router(user_router)
app.include_router(card_router)
app.include_router(transaction_router)
app.include_router(currency_router)