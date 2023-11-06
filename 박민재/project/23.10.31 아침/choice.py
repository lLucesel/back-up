import random
import MySQLdb
from detail import FoodDetail
from database import MySQLClientConnector
from pymysql import OperationalError
# choice는 메인 화면의 랜덤 추첨과 식단 추천에만 씀


class FoodChoice:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.food_detail = FoodDetail(db_name, user, password, host, port)

    def ran_side(self):
        try:
            _ran_side = self.food_detail.side_name()

            if len(_ran_side) < 3:
                return "Not enough side dishes."

            __ran_side = random.sample(_ran_side, 3)
            ___ran_side = [side["name"] for side in __ran_side]
            result = ", ".join(___ran_side)

            return result
        except OperationalError:
            return "No food_type_id = 1"
        except MySQLdb.Error as e:
            return f"Error food_type_id = 1: {e}"

    def ran_soup(self):
        try:
            _ran_soup = random.choice(self.food_detail.soup_name())
            return _ran_soup["name"]
        except OperationalError:
            return "No food_type_id = 2"
        except MySQLdb.Error as e:
            return f"Error food_type_id = 2: {e}"

    #def ran_cal(self):
    #    side = self.food_detail.side_diet()
    #    _side = random.sample(side, 3)
    #    soup = self.food_detail.soup_diet()
    #    _soup = random.choice(soup)
    #    try:
    #        _diet_sum = []
    #        for _diet_sum in range(7):
    #            _side_cal = [side_cal["calorie"] for side_cal in _side]
    #            _soup_cal = _soup["calorie"]
    #            _diet = sum(_side_cal) + _soup_cal
    #            if 2000 <= _diet <= 2300:
    #                return True
    #            else:
    #                return False
    #            __diet_sum = _diet_sum.append(_diet)





    def close_connection(self):
        self.connector.close()
