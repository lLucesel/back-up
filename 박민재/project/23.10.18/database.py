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
        self.curs.executemany(query, args)

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
    def side(self):
        side = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type_id = '1'
            """
        self.curs.execute(side)
        return self.curs.fetchall()

    # 반찬(food_type_id = 1)에서 해당하는 이름의 내용 불러오기
    def side_detail(self):
        side_detail = """
            SELECT ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type_id = '1'
            """
        self.curs.execute(side_detail)
        return self.curs.fetchall()

    # food table에서 국(food_type_id = 2) 불러오기
    def soup(self):
        soup = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type_id = '2'
            """
        self.curs.execute(soup)
        return self.curs.fetchall()

    # 국(food_type_id = 2)에서 해당하는 이름의 내용 불러오기
    def soup_detail(self):
        soup_detail = """
            SELECT ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type_id = '2'
            """
        self.curs.execute(soup_detail)
        return self.curs.fetchall()
