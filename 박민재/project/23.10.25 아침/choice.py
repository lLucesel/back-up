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

    #def ran_calorie(self):
    #    calorie_data = [row[0] for row in cursor.fetchall()]
#
    #    selected_calories = []
    #    total_calories = 0
#
    #    while total_calories <= 15000 and len(selected_calories) < 7:
    #        calorie = random.choice(calorie_data)
    #        if total_calories + calorie <= 15000:
    #            selected_calories.append(calorie)
    #            total_calories += calorie
#
    #    cursor.close()
    #    conn.close()


    def close_connection(self):
        self.connector.close()
