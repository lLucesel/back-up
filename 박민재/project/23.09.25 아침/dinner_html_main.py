from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # templates 디렉토리에 HTML 템플릿을 저장합니다.


@app.get("/", response_class=HTMLResponse)
async def dinner_main(request: Request):
    # HTML 템플릿 파일 (templates/home.html)을 렌더링합니다.
    return templates.TemplateResponse("dinner_main.html", {"request": request})


@app.get("/dinner_html_main_1", response_class=HTMLResponse)
async def dinner_main_side(request: Request):
    # 여기에서 "반찬/국 중 하나 고르기" 로직을 실행하고 결과를 HTML 템플릿에 전달합니다.
    result = "고른 메뉴: [여기에 선택 결과를 표시]"
    return templates.TemplateResponse("dinner_main_side.html", {"request": request, "result": result})
