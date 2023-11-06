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


a = _food_choice.ran_side()
c = _food_diet.diet_plan()

print(c)
_c = c[0]
print(c[0][1]["calorie"])
__c = _c[0]
___c = _c[3]
print(__c)
print(___c)
sum__c = _c[0]["calorie"] + _c[1]["calorie"]

print(a)
print(sum__c)
