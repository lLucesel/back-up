import random
import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from choice import FoodChoice
from detail import FoodDetail
from database import MySQLClientConnector
from diet import FoodDiet

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

_add = MySQLClientConnector(db_name, user, password, host, port)
_food_choice = FoodChoice(db_name, user, password, host, port)
_food_detail = FoodDetail(db_name, user, password, host, port)
_food_diet = FoodDiet(db_name, user, password, host, port)

_diet = _food_diet.diet_plan()

sun_side_cal = sum(_diet[0][0]["calorie"] + _diet[0][1]["calorie"] + _diet[0][2]["calorie"])
mon_side_cal = sum(_diet[1][0]["calorie"] + _diet[1][1]["calorie"] + _diet[1][2]["calorie"])
tue_side_cal = sum(_diet[2][0]["calorie"] + _diet[2][1]["calorie"] + _diet[2][2]["calorie"])
wed_side_cal = sum(_diet[3][0]["calorie"] + _diet[3][1]["calorie"] + _diet[3][2]["calorie"])
thu_side_cal = sum(_diet[4][0]["calorie"] + _diet[4][1]["calorie"] + _diet[4][2]["calorie"])
fri_side_cal = sum(_diet[5][0]["calorie"] + _diet[5][1]["calorie"] + _diet[5][2]["calorie"])
sat_side_cal = sum(_diet[6][0]["calorie"] + _diet[6][1]["calorie"] + _diet[6][2]["calorie"])
sun_soup_cal = sum(_diet[0][3]["calorie"])
mon_soup_cal = sum(_diet[1][3]["calorie"])
tue_soup_cal = sum(_diet[2][3]["calorie"])
wed_soup_cal = sum(_diet[3][3]["calorie"])
thu_soup_cal = sum(_diet[4][3]["calorie"])
fri_soup_cal = sum(_diet[5][3]["calorie"])
sat_soup_cal = sum(_diet[6][3]["calorie"])
sun_cal = sum(sun_side_cal + sun_soup_cal)
mon_cal = sum(mon_side_cal + mon_soup_cal)
tue_cal = sum(tue_side_cal + tue_soup_cal)
wed_cal = sum(wed_side_cal + wed_soup_cal)
thu_cal = sum(thu_side_cal + thu_soup_cal)
fri_cal = sum(fri_side_cal + fri_soup_cal)
sat_cal = sum(sat_side_cal + sat_soup_cal)
all_side = (
    sum(sun_side_cal + mon_side_cal + tue_side_cal + wed_side_cal + thu_side_cal + fri_side_cal + sat_side_cal))
all_soup = (
    sum(sun_soup_cal + mon_soup_cal + tue_soup_cal + wed_soup_cal + thu_soup_cal + fri_soup_cal + sat_soup_cal))
all_food = all_side + all_soup
print(all_food)
print("?")
sun_car = sum(_diet[0][0]["carbohydrate"] + _diet[0][1]["carbohydrate"] +
              _diet[0][2]["carbohydrate"] + _diet[0][3]["carbohydrate"])
mon_car = sum(_diet[1][0]["carbohydrate"] + _diet[1][1]["carbohydrate"] +
              _diet[1][2]["carbohydrate"] + _diet[1][3]["carbohydrate"])
tue_car = sum(_diet[2][0]["carbohydrate"] + _diet[2][1]["carbohydrate"] +
              _diet[2][2]["carbohydrate"] + _diet[2][3]["carbohydrate"])
wed_car = sum(_diet[3][0]["carbohydrate"] + _diet[3][1]["carbohydrate"] +
              _diet[3][2]["carbohydrate"] + _diet[3][3]["carbohydrate"])
thu_car = sum(_diet[4][0]["carbohydrate"] + _diet[4][1]["carbohydrate"] +
              _diet[4][2]["carbohydrate"] + _diet[4][3]["carbohydrate"])
fri_car = sum(_diet[5][0]["carbohydrate"] + _diet[5][1]["carbohydrate"] +
              _diet[5][2]["carbohydrate"] + _diet[5][3]["carbohydrate"])
sat_car = sum(_diet[6][0]["carbohydrate"] + _diet[6][1]["carbohydrate"] +
              _diet[6][2]["carbohydrate"] + _diet[6][3]["carbohydrate"])
all_car = sum(sun_car + mon_car + tue_car + wed_car + thu_car + fri_car + sat_car)
print(all_car)
print("?")
sun_pro = sum(_diet[0][0]["protein"] + _diet[0][1]["protein"] +
              _diet[0][2]["protein"] + _diet[0][3]["protein"])
mon_pro = sum(_diet[1][0]["protein"] + _diet[1][1]["protein"] +
              _diet[1][2]["protein"] + _diet[1][3]["protein"])
tue_pro = sum(_diet[2][0]["protein"] + _diet[2][1]["protein"] +
              _diet[2][2]["protein"] + _diet[2][3]["protein"])
wed_pro = sum(_diet[3][0]["protein"] + _diet[3][1]["protein"] +
              _diet[3][2]["protein"] + _diet[3][3]["protein"])
thu_pro = sum(_diet[4][0]["protein"] + _diet[4][1]["protein"] +
              _diet[4][2]["protein"] + _diet[4][3]["protein"])
fri_pro = sum(_diet[5][0]["protein"] + _diet[5][1]["protein"] +
              _diet[5][2]["protein"] + _diet[5][3]["protein"])
sat_pro = sum(_diet[6][0]["protein"] + _diet[6][1]["protein"] +
              _diet[6][2]["protein"] + _diet[6][3]["protein"])
all_pro = sum(sun_pro + mon_pro + tue_pro + wed_pro + thu_pro + fri_pro + sat_pro)
print(all_pro)
print("?")
sun_vit = sum(_diet[0][0]["vitamin"] + _diet[0][1]["vitamin"] +
              _diet[0][2]["vitamin"] + _diet[0][3]["vitamin"])
mon_vit = sum(_diet[1][0]["vitamin"] + _diet[1][1]["vitamin"] +
              _diet[1][2]["vitamin"] + _diet[1][3]["vitamin"])
tue_vit = sum(_diet[2][0]["vitamin"] + _diet[2][1]["vitamin"] +
              _diet[2][2]["vitamin"] + _diet[2][3]["vitamin"])
wed_vit = sum(_diet[3][0]["vitamin"] + _diet[3][1]["vitamin"] +
              _diet[3][2]["vitamin"] + _diet[3][3]["vitamin"])
thu_vit = sum(_diet[4][0]["vitamin"] + _diet[4][1]["vitamin"] +
              _diet[4][2]["vitamin"] + _diet[4][3]["vitamin"])
fri_vit = sum(_diet[5][0]["vitamin"] + _diet[5][1]["vitamin"] +
              _diet[5][2]["vitamin"] + _diet[5][3]["vitamin"])
sat_vit = sum(_diet[6][0]["vitamin"] + _diet[6][1]["vitamin"] +
              _diet[6][2]["vitamin"] + _diet[6][3]["vitamin"])
all_vit = sum(sun_vit + mon_vit + tue_vit + wed_vit + thu_vit + fri_vit + sat_vit)
print(all_vit)
print("?")

#side_name = ("두부조림")
#_side_details = _food_detail.side_detail(side_name)
#_side_nutrients = _food_detail.side_nutrient(side_name)
#for __side_details in _side_details:
#    print(__side_details)
#for __side_nutrients in _side_nutrients:
#    print(__side_nutrients)
