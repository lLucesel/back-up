import MySQLdb
from MySQLdb.cursors import DictCursor


class MySQLClientConnector:
    def __init__(self, schema_nm, user_nm, password, host, port):
        self.conn = MySQLdb.connect(
            host=host,
            port=int(port),
            user=user_nm,
            password=password,
            db=schema_nm,
            charset='utf8mb4'
        )
        self.curs = self.conn.cursor(DictCursor)

    def executemany(self, query=None, args=None):
        return self.curs.executemany(query, args)

    def execute(self, query=None, args=None):
        return self.curs.execute(query, args)

    def fetchone(self, query=None, args=None):
        self.curs.execute(query, args)
        return self.curs.fetchone()

    def fetchall(self, query=None, args=None):
        self.curs.execute(query, args)
        return self.curs.fetchall()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()

    # food table에서 반찬(food_type_id = 1) 불러오기
    # side는 이름 관련 코드에서 씀. choice.py random, detail.py name
    def side(self):
        side = """
        SELECT *
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type = '반찬'
        """
        self.curs.execute(side)
        return self.curs.fetchone()

    def soup(self):
        soup = """
        SELECT *
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type = '국' 
        """
        self.curs.execute(soup)
        return self.curs.fetchone()

    def side_name(self):
        side_name = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬' 
            """
        self.curs.execute(side_name)
        return self.curs.fetchall()

    # 반찬(food_type_id = 1)에서 해당하는 이름의 내용 불러오기
    # side_detail은 detail.py에서 ingredient, spice, recipe를 따로 따로 불러내기 위해 씀
    def side_detail(self):
        side_detail = """
            SELECT ingredient, spice, recipe
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬'
            """
        self.curs.execute(side_detail)
        return self.curs.fetchone()

    # 반찬(food_type_id = 1)에서 해당하는 이름의 내용 불러오기
    # side_detail은 detail.py에서 calorie, carbohydrate, protein, vitamin를 따로 따로 불러내기 위해 씀
    def side_nutrient(self):
        side_nutrient = """
            SELECT calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬' 
            """
        self.curs.execute(side_nutrient)
        return self.curs.fetchone()

    # food table에서 국(food_type_id = 2) 불러오기
    # soup는 이름 관련 코드에서 씀. choice.py random, detail.py name
    def soup_name(self):
        soup_name = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' 
            """
        self.curs.execute(soup_name)
        return self.curs.fetchall()

    # def soup_name_v2(self, type_id):
    #    soup = """
    #        SELECT name
    #        FROM food JOIN food_type ON food.food_type_id = food_type.id
    #        WHERE food_type_id =
    #        """
    #    self.curs.execute(soup, (type_id,))
    #    return self.curs.fetchall()

    # 국(food_type_id = 2)에서 해당하는 이름의 내용 불러오기
    # soup_detail은 detail.py에서 ingredient, spice, recipe를 따로 따로 불러내기 위해 씀
    def soup_detail(self):
        soup_detail = """
            SELECT ingredient, spice, recipe
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' 
            """
        self.curs.execute(soup_detail)
        return self.curs.fetchone()

    # 반찬(food_type_id = 1)에서 해당하는 이름의 내용 불러오기
    # soup_detail은 detail.py에서 calorie, carbohydrate, protein, vitamin를 따로 따로 불러내기 위해 씀
    def soup_nutrient(self):
        soup_nutrient = """
        SELECT calorie, carbohydrate, protein, vitamin
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type = '국' 
        """
        self.curs.execute(soup_nutrient)
        return self.curs.fetchone()

    def side_diet(self):
        _side_diet = """
        SELECT name, calorie, carbohydrate, protein, vitamin
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type = '반찬'
        """
        self.curs.excute(_side_diet)
        return self.curs.fetchall()

    def soup_diet(self):
        _soup_diet = """
        SELECT name, calorie, carbohydrate, protein, vitamin
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type = '국'
        """
        self.curs.execute(_soup_diet)
        return self.curs.fetchall()

    def food_cal(self):
        _food_cal = """
        SELECT name, calorie
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        """
        self.curs.excute(_food_cal)
        return self.curs.fetchall()

    # food table 전체


# sql = "insert into food (food_type_id, name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin)
# values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
# val = [('a','a','a','a','a','a','a','a','a')]


#if __name__ == '__main__':
#   MySQLClientConnector
