from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from lotto import FoodChoice


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.get("/get_random_foods")
async def random_foods():
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306

    random_food = FoodChoice(db_name, user, password, host, port)

    ran_side_name = random_food.side()
    ran_soup_name = random_food.soup()

    random_food.close_connection()

    return {"side": ran_side_name, "soup": ran_soup_name}
