from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def dinner_html_main(request: Request):
    return templates.TemplateResponse("dinner_html_main.html", {"request": request})


@app.get("/choose_dish", response_class=HTMLResponse)
async def choose_dish(request: Request):
    result = "고른 메뉴: [여기에 선택 결과를 표시]"
    return templates.TemplateResponse("choose_dish.html", {"request": request, "result": result})


@app.get("/dinner_html_main_1", response_class=HTMLResponse)
async def dinner_html_main_1(request: Request):
    return RedirectResponse(url="/dinner_html_main_1.html")
