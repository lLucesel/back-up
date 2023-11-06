import random
import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from choice import FoodChoice
from detail import FoodDetail
from database import MySQLClientConnector

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

_add = MySQLClientConnector(db_name, user, password, host, port)
_food_choice = FoodChoice(db_name, user, password, host, port)
_food = FoodDetail(db_name, user, password, host, port)
side_name = ("두부조림")
_side_details = _food.side_detail(side_name)
_side_nutrients = _food.side_nutrient(side_name)
for __side_details in _side_details:
    print(__side_details)
for __side_nutrients in _side_nutrients:
    print(__side_nutrients)


#side = self.food_detail.side_diet()
#_side = random.sample(side, 3)
#soup = self.food_detail.soup_diet()
#_soup = random.choice(soup)
#try:
#    _diet_sum = []
#    for _diet_sum in range(7):
#        _side_cal = [side_cal["calorie"] for side_cal in _side]
#        _soup_cal = _soup["calorie"]
#        _diet = sum(_side_cal) + _soup_cal
#        if 2000 <= _diet <= 2300:
#            return True
#        else:
#            return False
#        __diet_sum = _diet_sum.append(_diet)