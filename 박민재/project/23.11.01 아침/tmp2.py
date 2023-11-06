from choice import FoodChoice
from database import MySQLClientConnector
from diet import FoodDiet

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

_add = MySQLClientConnector(db_name, user, password, host, port)
_food_choice = FoodChoice(db_name, user, password, host, port)
_food_diet = FoodDiet(db_name, user, password, host, port)

_food_diet.diet_set()
