import random
import MySQLdb
from database import MySQLClientConnector
from detail import FoodDetail
from choice import FoodChoice
from pymysql import OperationalError


class FoodDiet:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.food_detail = FoodDetail(db_name, user, password, host, port)
        self.food_choice = FoodChoice(db_name, user, password, host, port)
        self.diet_plans = []

    def diet_plan(self):
        while len(self.diet_plans) < 7:
            _diet_set = self.diet_set()
            if self.valid_diet_set(_diet_set):
                self.diet_plans.append(_diet_set)

    def diet_set(self):
        diet_set = []
        try:
            while True:
                _diet_side = self.food_choice.diet_side()
                _diet_soup = self.food_choice.diet_soup()
                diet_set.extend([_diet_side, _diet_soup])
                sum_cal = sum(food["calorie"] for food in diet_set)
                if 2000 <= sum_cal <= 2300:
                    break
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def valid_diet_set(self, diet_set):
        diet_names = set(diet["name"] for diet in self.diet_plans)
        for food in diet_set:
            if food["name"] in diet_names:
                return False
        return True

    def close_connection(self):
        self.connector.close()
