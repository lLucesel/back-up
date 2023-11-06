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
__diet = _diet[0]

sun_side_cal = _diet[0][0]["calorie"] + _diet[0][1]["calorie"] + _diet[0][2]["calorie"]
mon_side_cal = _diet[1][4]["calorie"] + _diet[1][5]["calorie"] + _diet[1][6]["calorie"]
tue_side_cal = _diet[2][8]["calorie"] + _diet[2][9]["calorie"] + _diet[2][10]["calorie"]
wed_side_cal = _diet[3][12]["calorie"] + _diet[3][13]["calorie"] + _diet[3][14]["calorie"]
thu_side_cal = _diet[4][16]["calorie"] + _diet[4][17]["calorie"] + _diet[4][18]["calorie"]
fri_side_cal = _diet[5][20]["calorie"] + _diet[5][21]["calorie"] + _diet[5][22]["calorie"]
sat_side_cal = _diet[6][24]["calorie"] + _diet[6][25]["calorie"] + _diet[6][26]["calorie"]
sun_soup_cal = _diet[0][3]["calorie"]
mon_soup_cal = _diet[1][7]["calorie"]
tue_soup_cal = _diet[2][11]["calorie"]
wed_soup_cal = _diet[3][15]["calorie"]
thu_soup_cal = _diet[4][19]["calorie"]
fri_soup_cal = _diet[5][23]["calorie"]
sat_soup_cal = _diet[6][27]["calorie"]
sun_cal = sun_side_cal + sun_soup_cal
mon_cal = mon_side_cal + mon_soup_cal
tue_cal = tue_side_cal + tue_soup_cal
wed_cal = wed_side_cal + wed_soup_cal
thu_cal = thu_side_cal + thu_soup_cal
fri_cal = fri_side_cal + fri_soup_cal
sat_cal = sat_side_cal + sat_soup_cal
all_side = sun_side_cal + mon_side_cal + tue_side_cal + wed_side_cal + thu_side_cal + fri_side_cal + sat_side_cal
all_soup = sun_soup_cal + mon_soup_cal + tue_soup_cal + wed_soup_cal + thu_soup_cal + fri_soup_cal + sat_soup_cal
all_food = all_side + all_soup
print(all_side)
print(all_soup)
print(all_food)
print("?")
sun_car = (_diet[0][0]["carbohydrate"] + _diet[0][1]["carbohydrate"] +
           _diet[0][2]["carbohydrate"] + _diet[0][3]["carbohydrate"])
mon_car = (_diet[1][0]["carbohydrate"] + _diet[1][1]["carbohydrate"] +
           _diet[1][2]["carbohydrate"] + _diet[1][3]["carbohydrate"])
tue_car = (_diet[2][0]["carbohydrate"] + _diet[2][1]["carbohydrate"] +
           _diet[2][2]["carbohydrate"] + _diet[2][3]["carbohydrate"])
wed_car = (_diet[3][0]["carbohydrate"] + _diet[3][1]["carbohydrate"] +
           _diet[3][2]["carbohydrate"] + _diet[3][3]["carbohydrate"])
thu_car = (_diet[4][0]["carbohydrate"] + _diet[4][1]["carbohydrate"] +
           _diet[4][2]["carbohydrate"] + _diet[4][3]["carbohydrate"])
fri_car = (_diet[5][0]["carbohydrate"] + _diet[5][1]["carbohydrate"] +
           _diet[5][2]["carbohydrate"] + _diet[5][3]["carbohydrate"])
sat_car = (_diet[6][0]["carbohydrate"] + _diet[6][1]["carbohydrate"] +
           _diet[6][2]["carbohydrate"] + _diet[6][3]["carbohydrate"])
all_car = sun_car + mon_car + tue_car + wed_car + thu_car + fri_car + sat_car
print(all_car)
print("?")
sun_pro = (_diet[0][0]["protein"] + _diet[0][1]["protein"] +
           _diet[0][2]["protein"] + _diet[0][3]["protein"])
mon_pro = (_diet[1][0]["protein"] + _diet[1][1]["protein"] +
           _diet[1][2]["protein"] + _diet[1][3]["protein"])
tue_pro = (_diet[2][0]["protein"] + _diet[2][1]["protein"] +
           _diet[2][2]["protein"] + _diet[2][3]["protein"])
wed_pro = (_diet[3][0]["protein"] + _diet[3][1]["protein"] +
           _diet[3][2]["protein"] + _diet[3][3]["protein"])
thu_pro = (_diet[4][0]["protein"] + _diet[4][1]["protein"] +
           _diet[4][2]["protein"] + _diet[4][3]["protein"])
fri_pro = (_diet[5][0]["protein"] + _diet[5][1]["protein"] +
           _diet[5][2]["protein"] + _diet[5][3]["protein"])
sat_pro = (_diet[6][0]["protein"] + _diet[6][1]["protein"] +
           _diet[6][2]["protein"] + _diet[6][3]["protein"])
all_pro = sun_pro + mon_pro + tue_pro + wed_pro + thu_pro + fri_pro + sat_pro
print(all_pro)
print("?")
sun_vit = (_diet[0][0]["vitamin"] + _diet[0][1]["vitamin"] +
           _diet[0][2]["vitamin"] + _diet[0][3]["vitamin"])
mon_vit = (_diet[1][0]["vitamin"] + _diet[1][1]["vitamin"] +
           _diet[1][2]["vitamin"] + _diet[1][3]["vitamin"])
tue_vit = (_diet[2][0]["vitamin"] + _diet[2][1]["vitamin"] +
           _diet[2][2]["vitamin"] + _diet[2][3]["vitamin"])
wed_vit = (_diet[3][0]["vitamin"] + _diet[3][1]["vitamin"] +
           _diet[3][2]["vitamin"] + _diet[3][3]["vitamin"])
thu_vit = (_diet[4][0]["vitamin"] + _diet[4][1]["vitamin"] +
           _diet[4][2]["vitamin"] + _diet[4][3]["vitamin"])
fri_vit = (_diet[5][0]["vitamin"] + _diet[5][1]["vitamin"] +
           _diet[5][2]["vitamin"] + _diet[5][3]["vitamin"])
sat_vit = (_diet[6][0]["vitamin"] + _diet[6][1]["vitamin"] +
           _diet[6][2]["vitamin"] + _diet[6][3]["vitamin"])
all_vit = sun_vit + mon_vit + tue_vit + wed_vit + thu_vit + fri_vit + sat_vit
print(all_vit)
print("?")

#side_name = ("두부조림"
#_side_details = _food_detail.side_detail(side_name
#_side_nutrients = _food_detail.side_nutrient(side_name
#for __side_details in _side_details:
#    print(__side_details
#for __side_nutrients in _side_nutrients:
#    print(__side_nutrients
