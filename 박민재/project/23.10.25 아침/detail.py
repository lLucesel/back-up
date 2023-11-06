import MySQLdb
from database import MySQLClientConnector
from pymysql import OperationalError


class FoodDetail:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.side_name = self.connector.side_name()
        self.soup_name = self.connector.soup_name()
        self.side_detail = self.connector.side_detail()
        self.soup_detail = self.connector.soup_detail()
        self.side_nutrient = self.connector.side_nutrient()
        self.soup_nutrient = self.connector.soup_nutrient()

    # ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
    def side_name(self):
        try:
            return self.side_name
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def soup_name(self):
        try:
            return self.soup_name
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    # side_detail 은 ingredient, spice, recipe 를 합쳐 놓은것
    def side_detail(self):
        try:
            _detail = self.side_detail
            _side_ingredient = _detail["ingredient"]
            _side_spice = _detail["spice"]
            _side_recipe = _detail["recipe"]
            return _side_ingredient, _side_spice, _side_recipe
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    # soup_detail 은 ingredient, spice, recipe 를 합쳐 놓은것
    def soup_detail(self):
        try:
            _detail = self.soup_detail
            _soup_ingredient = _detail["ingredient"]
            _soup_spice = _detail["spice"]
            _soup_recipe = _detail["recipe"]
            return _soup_ingredient, _soup_spice, _soup_recipe
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    # nutrient는 side_detail에서 calorie, carbohydrate, protein, vitamin를 합쳐서 부른다
    def side_nutrient(self):
        try:
            _nutrient = self.side_nutrient
            _side_calorie = _nutrient["calorie"]
            _side_carbohydrate = _nutrient["carbohydrate"]
            _side_protein = _nutrient["protein"]
            _side_vitamin = _nutrient["vitamin"]
            return _side_calorie, _side_carbohydrate, _side_protein, _side_vitamin
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    # nutrient는 soup_detail에서 calorie, carbohydrate, protein, vitamin를 합쳐서 부른다
    def soup_nutrient(self):
        try:
            _nutrient = self.soup_nutrient
            _soup_calorie = _nutrient["calorie"]
            _soup_carbohydrate = _nutrient["carbohydrate"]
            _soup_protein = _nutrient["protein"]
            _soup_vitamin = _nutrient["vitamin"]
            return _soup_calorie, _soup_carbohydrate, _soup_protein, _soup_vitamin
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def food(self):
        try:
            _food = self.food()
            _food_type_id = _food["food_type_id"]
            _name = _food["name"]
            _ingredient = _food["ingredient"]
            _spice = _food["spice"]
            _recipe = _food["recipe"]
            _calorie = _food["calorie"]
            _protein = _food["protein"]
            _vitamin = _food["vitamin"]
            return _food_type_id, _name, _ingredient, _spice, _recipe, _calorie, _protein, _vitamin
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    # def add_food(self):
    #    add_food = """
    #                INSERT INTO food (food_type_id, name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin)
    #                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    #            """
    #    values = (food_type_id, name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin)

    def close_connection(self):
        self.connector.close()
