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


if __name__ == '__main__':
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306

    connector = MySQLClientConnector(db_name, user, password, host, 3306)

    # food table에서 반찬(food_type_id = 1) 불러오기
    side = """
        SELECT name
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type_id = '1'
        """

    # 반찬(food_type_id = 1)에서 해당하는 이름의 내용 불러오기
    side_detail = """
        SELECT name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type_id = '1'
    """

    # food table에서 국(food_type_id = 2) 불러오기
    soup = """
        SELECT name
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type_id = '2'
        """

    # 국(food_type_id = 2)에서 해당하는 이름의 내용 불러오기
    soup_detail = """
           SELECT name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
           FROM food JOIN food_type ON food.food_type_id = food_type.id
           WHERE food_type_id = '2'
           """

    diet = """
        SELECT name, calorie, carbohydrate, protein, vitamin
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        """

    result_side = connector.fetchall(side)
    result_side_detail = connector.fetchall(side_detail)
    result_soup = connector.fetchall(soup)
    result_soup_detail = connector.fetchall(soup_detail)
    result_diet = connector.fetchall(diet)

    connector.close()
