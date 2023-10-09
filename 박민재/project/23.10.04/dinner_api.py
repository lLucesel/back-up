from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from dinner_db import SessionLocal, Food, FoodType

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("dinner_main.html", {"request": request})


@app.get("/dinner_side")
async def read_dinner_side(request: Request):
    db: Session = SessionLocal()

    # 데이터베이스에서 food_type_id가 1인 반찬 정보를 조회
    food_list = db.query(Food).join(FoodType).filter(FoodType.food_type == '반찬').all()

    db.close()

    return templates.TemplateResponse("dinner_side.html", {"request": request, "food_list": food_list})


@app.get("/dinner_soup")
async def read_dinner_soup(request: Request):
    db: Session = SessionLocal()

    # 데이터베이스에서 food_type_id가 2인 국 정보를 조회
    food_list = db.query(Food).join(FoodType).filter(FoodType.food_type == '국').all()

    db.close()

    return templates.TemplateResponse("dinner_soup.html", {"request": request, "food_list": food_list})
