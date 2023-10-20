import random
import MySQLdb
from database import MySQLClientConnector

if __name__ == '__main__':
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306

    connector = MySQLClientConnector(db_name, user, password, host, 3306)

    try:
        try:
            result_side = connector.side()
            if result_side:
                random_side = random.choice(result_side)
                random_side_name = random_side["name"]
                print(random_side_name)
            else:
                print("No food_type_id = 1")
        except MySQLdb.Error as e:
            print(f"Error food_type_id = 1: {e}")

        try:
            result_soup = connector.soup()
            if result_soup:
                random_soup = random.choice(result_soup)
                random_soup_name = random_soup["name"]
            else:
                print("No food_type_id = 2")
        except MySQLdb.Error as e:
            print(f"Error food_type_id = 2: {e}")
    except MySQLdb.Error as e:
        print(f"Database connection error: {e}")
    finally:
        connector.close()
