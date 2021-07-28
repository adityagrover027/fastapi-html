from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from src.model import spell_number

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return 'HTML App with FastAPI'


@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    name = "Type a name"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'name': name})


@app.post("/form")
def form_post(request: Request, num: int = Form(...), name: str = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'name': name})