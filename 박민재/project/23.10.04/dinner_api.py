from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dinner_db import Base, FoodType, Food

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DATABASE_URL = "mysql://admin_mj:77gundam77@127.0.0.1/C:/E drive/강남구 AWS 교육/파이썬 놀이_본/박민재/project/mysql/dinner_db?charset=utf8"
engine = create_engine(DATABASE_URL, encoding="utf-8", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("dinner_main.html", {"request": request})


@app.get("/dinner_side")
async def read_dinner_side(request: Request):
    # 데이터베이스에서 food_type_id가 1인 정보들을 조회
    db = SessionLocal()
    food_list = db.query(Food).join(FoodType).filter(FoodType.food_type_id == 1).all()
    db.close()
    return templates.TemplateResponse("dinner_side.html", {"request": request, "food_list": food_list})


@app.get("/dinner_soup")
async def read_dinner_soup(request: Request):
    # 데이터베이스에서 food_type_id가 2인 정보들을 조회
    db = SessionLocal()
    food_list = db.query(Food).join(FoodType).filter(FoodType.food_type_id == 2).all()
    db.close()
    return templates.TemplateResponse("dinner_main_side.html", {"request": request, "food_list": food_list})


@app.post("/diet")
async def diet(request: Request):
    return templates.TemplateResponse("dinner_diet.html", {"request": request, "selected_menu": "식단짜기"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
