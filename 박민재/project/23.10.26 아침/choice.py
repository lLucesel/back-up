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
            _ran_side = random.choice(self.connector.side_name())
            return _ran_side["name"]
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

    def man_calorie(self):
        _side_cal = self.connector.side_cal()
        _soup_cal = self.connector.soup_cal()

        _side_cal_data = [row[0] for row in _side_cal]
        _soup_cal_data = [row[0] for row in _soup_cal()]

        _choice_side = []
        _choice_soup = []
        _total_side = 0
        _total_soup = 0



    def man_calorie(self):
        _side_data = [row[0] for row in self.connector.side_cal()]
        _soup_data = [row[0] for row in self.connector.soup_cal()]

        _choice_side_man = []
        _choice_soup_man = []
        _total_side_calories = 0
        _total_soup_calories = 0

        while 7000 <= total_calories <= 8000 and len(choice_man) < 7:
            calorie = random.choice(man_data)
            if total_calories + calorie < 7000:
                choice_man.append(calorie)
                total_calories += calorie
        
    def woman_calorie(self):
        woman_data = [row[0] for row in self.connector.cal()]
        choice_woman = []
        total_calories = 0

        while 6500 <= total_calories <= 7500 and len(choice_woman) < 7:
            calorie = random.choice(woman_data)
            if total_calories + calorie < 6500:
                choice_woman.append(calorie)
                total_calories += calorie


    def close_connection(self):
        self.connector.close()
