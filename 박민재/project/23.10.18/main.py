from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from lotto import FoodChoice
from detail import FoodDetail

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306
    random_food = FoodChoice(db_name, user, password, host, port)
    side_name = random_food.side()
    soup_name = random_food.soup()
    random_food.close_connection()
    return (templates.TemplateResponse
            ("main.html", {"request": request, "side_name": side_name, "soup_name": soup_name}))


@app.get("/side")
async def side(request: Request):
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306
    food = FoodDetail(db_name, user, password, host, port)
    name_side = food.side_name
    name_side = sorted(name_side, key=lambda x: x["name"])
    return (templates.TemplateResponse
            ("side.html", {"request": request, "name_side": name_side}))


@app.get("/side/{side_name}")
async def side_recipe(request: Request, side_name: str):
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306

    food = FoodDetail(db_name, user, password, host, port)

    side_ingredient = food.side_ingredient
    side_spice = food.side_spice
    side_recipe = food.side_recipe
    side_nutrient = food.side_nutrient

    return (templates.TemplateResponse
            ("side_recipe.html",
             {"request": request,
              "side_name": side_name,
              "side_ingredient": side_ingredient,
              "side_spice": side_spice,
              "side_recipe": side_recipe,
              "side_nutrient": side_nutrient
              }))


@app.get("/soup")
async def soup(request: Request):
    db_name = "dinner"
    user = "admin_mj"
    password = "77gundam77"
    host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
    port = 3306
    food = FoodDetail(db_name, user, password, host, port)
    name_soup = food.soup_name
    name_soup = sorted(name_soup, key=lambda x: x["name"])
    return (templates.TemplateResponse
            ("soup.html", {"request": request, "name_soup": name_soup}))
