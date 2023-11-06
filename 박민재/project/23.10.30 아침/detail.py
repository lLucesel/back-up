import MySQLdb
from database import MySQLClientConnector
from pymysql import OperationalError


class FoodDetail:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.side_names = self.connector.side_name()
        self.soup_names = self.connector.soup_name()
        self.side_details = self.connector.side_detail()
        self.soup_details = self.connector.soup_detail()
        self.side_nutrients = self.connector.side_nutrient()
        self.soup_nutrients = self.connector.soup_nutrient()

    def side_name(self):
        try:
            return self.side_names
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def soup_name(self):
        try:
            return self.soup_names
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def side_detail(self):
        try:
            return self.side_details
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def soup_detail(self):
        try:
            return self.soup_details
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def side_nutrient(self):
        try:
            return self.side_nutrients
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def soup_nutrient(self):
        try:
            return self.soup_nutrients
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def food(self):
        try:
            food_data = self.connector.side_name()  # Change to the correct method and data you want to retrieve
            return food_data
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error food: {e}"

    def side_ingredients_by_name(self, side_name):
        query = """
        SELECT ingredient
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 1"""
        return self.connector.execute(query, (side_name,))

    def side_spices_by_name(self, side_name):
        query = """
        SELECT spice
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 1"""
        return self.connector.execute(query, (side_name,))

    def side_recipe_by_name(self, side_name):
        query = """
        SELECT recipe
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 1"""
        return self.connector.execute(query, (side_name,))

    def side_nutrients_by_name(self, side_name):
        query = """
        SELECT calorie, carbohydrate, protein, vitamin
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 1"""
        result = self.connector.execute(query, (side_name,))
        return {
            "calorie": result[0]["calorie"],
            "carbohydrate": result[0]["carbohydrate"],
            "protein": result[0]["protein"],
            "vitamin": result[0]["vitamin"]
        }

    def soup_ingredients_by_name(self, soup_name):
        query = """
        SELECT ingredient
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 2"""
        return self.connector.execute(query, (soup_name,))

    def soup_spices_by_name(self, soup_name):
        query = """
        SELECT spice
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 2"""
        return self.connector.execute(query, (soup_name,))

    def soup_recipe_by_name(self, soup_name):
        query = """
        SELECT recipe
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 2"""
        return self.connector.execute(query, (soup_name,))

    def soup_nutrients_by_name(self, soup_name):
        query = """
        SELECT calorie, carbohydrate, protein, vitamin
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s AND food_type_id = 2"""
        result = self.connector.execute(query, (soup_name,))
        return {
            "calorie": result[0]["calorie"],
            "carbohydrate": result[0]["carbohydrate"],
            "protein": result[0]["protein"],
            "vitamin": result[0]["vitamin"]
        }

    def close_connection(self):
        self.connector.close()
