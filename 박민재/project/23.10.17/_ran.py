import random
from database import MySQLClientConnector

if __name__ == '__main__':
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306

    # MySQLClientConnector 인스턴스 생성
    connector = MySQLClientConnector(db_name, user, password, host, 3306)
    result_side = connector.side()
    result_soup = connector.soup()

    if result_side:
        random_side = random.choice(result_side)
        random_side_name = random_side["name"]
        print(f"Randomly selected food name with food_type_id = 1: {random_side_name}")
    else:
        print("No items found with food_type_id = 1")

    if result_soup:
        random_soup = random.choice(result_soup)
        random_soup_name = random_soup["name"]
        print(f"Randomly selected food name with food_type_id = 2: {random_soup_name}")
    else:
        print("No items found with food_type_id = 2")

    connector.close()
