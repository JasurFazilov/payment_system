from fastapi import APIRouter, Request
from main import template

html_router = APIRouter(prefix='/web', tags=['Example for front'])



@html_router.get('/')
async def hello_page(request: Request):
    return template.TemplateResponse('index.html', context={'request': request})


