import random
import MySQLdb
from database import MySQLClientConnector


class FoodChoice:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)

    def side(self):
        try:
            select_side = self.connector.side()
            if select_side:
                ran_side = random.choice(select_side)
                ran_side_name = ran_side["name"]
                return ran_side_name
            else:
                return "No food_type_id = 1"
        except MySQLdb.Error as e:
            return f"Error food_type_id = 1: {e}"

    def soup(self):
        try:
            select_soup = self.connector.soup()
            if select_soup:
                ran_soup = random.choice(select_soup)
                ran_soup_name = ran_soup["name"]
                return ran_soup_name
            else:
                return "No food_type_id = 2"
        except MySQLdb.Error as e:
            return f"Error food_type_id = 2: {e}"

    def close_connection(self):
        self.connector.close()
