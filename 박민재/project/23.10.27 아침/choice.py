import random
import MySQLdb
from detail import FoodDetail
from database import MySQLClientConnector
from pymysql import OperationalError


class FoodChoice:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)

    def ran_side(self):
        try:
            _ran_side = self.connector.side_name()

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
            _ran_soup = random.choice(self.connector.soup_name())
            return _ran_soup["name"]
        except OperationalError:
            return "No food_type_id = 2"
        except MySQLdb.Error as e:
            return f"Error food_type_id = 2: {e}"
        
    def man_side_calorie(self):
        man_side_diet = self.connector.side_diet()
        man_soup_diet = self.connector.soup_diet()
        total_cal = 0
        choice_side = []

        #_man_side_diet = man_side_diet["name"]
        #_man_side_diet = man_side_diet["name"]
        #_man_side_diet = man_side_diet["name"]
        #_man_side_diet = man_soup_diet["name"]
        
        while total_cal < 6000 or total_cal > 7000:
            ran_food_diet = random.sample(man_side_diet["name"], man_side_diet["name"], man_side_diet["name"], man_soup_diet["name"])
        


    #def man_side_calorie(self):
    #    total_calories = 0
    #    selected_foods = []
#
    #    while total_calories < 6000 or total_calories > 7000:
    #        random_food = random.choice(
    #            [self.connector.side_name(), self.connector.side_name(), self.connector.side_name(),
    #             self.connector.soup_name()])
#
    #        food_calories = random_food["calorie"]
    #        total_calories += food_calories
#
    #        selected_foods.append(random_food)
#
    #    return selected_foods, total_calories

    def woman_side_calorie(self):
        woman_data = [row[0] for row in self.connector.cal()]
        choice_woman = []
        total_calories = 0

        while 6500 <= total_calories <= 7500 and len(choice_woman) < 7:
            calorie = random.choice(woman_data)
            if total_calories + calorie < 6500:
                choice_woman.append(calorie)
                total_calories += calorie

    #def calorie(self):


    def close_connection(self):
        self.connector.close()
