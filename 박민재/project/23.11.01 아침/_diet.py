import random
import MySQLdb
from detail import FoodDetail
from database import MySQLClientConnector
from pymysql import OperationalError


class FoodDieta:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.food_detail = FoodDetail(db_name, user, password, host, port)

    def _diet_plan(self):
        _diet_plan = []
        for _ in range(7):
            _diet_set = set()
            sum_cal = 0
            
            while len(_diet_set) < 3:
                side = random.choice(self.food_detail.side_diet())
                if side["name"] not in _diet_set:
                    _diet_set.add(side["name"])
                    sum_cal += side["calorie"]
                    
            soup = random.choice(self.food_detail.soup_diet())
            _diet_set.add(soup["name"])
            sum_cal += soup["calorie"]
            
            if 2000 <= sum_cal <= 2300 and _diet_set not in _diet_plan:
                _diet_plan.append(_diet_set)

        return _diet_plan
