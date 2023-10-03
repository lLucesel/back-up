import sys
sys.path.append("..")
from fastapi import Depends, HTTPException, APIRouter, Request, FastAPI
import models
from database import engine, SessionLocal

from fastapi.responses import HTMLResponse
#템플릿 엔진 삽입
from fastapi.templating import Jinja2Templates

app = FastAPI()


router = APIRouter(
    prefix="/todos",
    tags=['todos'],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

#템플릿 변수에 templates 디렉터리 추가
templates = Jinja2Templates(directory="templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#templates 디렉터리의 home.html 호출
@router.get("/test")
async def test(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})