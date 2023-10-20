import MySQLdb
from database import MySQLClientConnector
from pymysql import OperationalError


class FoodDetail:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.side_name = self.connector.side()
        self.soup_name = self.connector.soup()
        self.select_side = self.connector.side_detail()
        self.select_soup = self.connector.soup_detail()

    def side_name(self):
        try:
            side_name_detail = self.side_name["name"]
            return side_name_detail
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    # ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
    def side_ingredient(self):
        try:
            side_ingredient = self.select_side["ingredient"]
            return side_ingredient
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error ingredient: {e}"

    def side_spice(self):
        try:
            side_spice = self.select_side["spice"]
            return side_spice
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error spice: {e}"

    def side_recipe(self):
        side_recipe = self.connector.side_detail()
        try:
            side_recipe = side_recipe["recipe"]
            return side_recipe
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error recipe: {e}"

    # nutrient는 side_detail에서 calorie, carbohydrate, protein, vitamin를 합쳐서 부른다
    def side_nutrient(self):
        side_nutrient = self.connector.side_detail()
        try:
            side_nutrient_calorie = side_nutrient["calorie"]
            side_nutrient_carbohydrate = side_nutrient["carbohydrate"]
            side_nutrient_protein = side_nutrient["protein"]
            side_nutrient_vitamin = side_nutrient["vitamin"]
            return side_nutrient_calorie, side_nutrient_carbohydrate, side_nutrient_protein, side_nutrient_vitamin
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def soup_name(self):
        try:
            soup_name = self.soup_name()
            soup_name_detail = soup_name["name"]
            return soup_name_detail
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    # ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
    def soup_ingredient(self):
        try:
            soup_ingredient = self.select_soup["ingredient"]
            return soup_ingredient
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error ingredient: {e}"

    def soup_spice(self):
        try:
            soup_spice = self.select_soup["spice"]
            return soup_spice
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error spice: {e}"

    def soup_recipe(self):
        soup_recipe = self.connector.soup_detail()
        try:
            soup_recipe = soup_recipe["recipe"]
            return soup_recipe
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error recipe: {e}"

    # nutrient는 soup_detail에서 calorie, carbohydrate, protein, vitamin를 합쳐서 부른다
    def soup_nutrient(self):
        soup_nutrient = self.connector.soup_detail()
        try:
            soup_nutrient_calorie = soup_nutrient["calorie"]
            soup_nutrient_carbohydrate = soup_nutrient["carbohydrate"]
            soup_nutrient_protein = soup_nutrient["protein"]
            soup_nutrient_vitamin = soup_nutrient["vitamin"]
            return soup_nutrient_calorie, soup_nutrient_carbohydrate, soup_nutrient_protein, soup_nutrient_vitamin
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def close_connection(self):
        self.connector.close()
