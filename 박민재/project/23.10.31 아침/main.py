import random
import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from choice import FoodChoice
from detail import FoodDetail
from database import MySQLClientConnector

app = FastAPI()
templates = Jinja2Templates(directory="templates")

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

_add = MySQLClientConnector(db_name, user, password, host, port)
_food_choice = FoodChoice(db_name, user, password, host, port)
_food = FoodDetail(db_name, user, password, host, port)


@app.get("/")
async def main(request: Request):
    ran_side_name = _food_choice.ran_side()
    ran_soup_name = _food_choice.ran_soup()

    return (templates.TemplateResponse
            ("main.html", {"request": request,
                           "side_name": ran_side_name,
                           "soup_name": ran_soup_name}))


@app.get("/side")
async def side(request: Request):
    _side_name = _food.side_name()
    _side_name = sorted(_side_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("side.html", {"request": request, "side_name": _side_name}))


@app.get("/soup")
async def soup(request: Request):
    _soup_name = _food.soup_name()
    _soup_name = sorted(_soup_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("soup.html", {"request": request, "soup_name": _soup_name}))


@app.get("/side/{side_name}")
async def side_recipe(request: Request, side_name: str):
    # 클릭해서 들어간 side_name에 해당하는 요소들을 갖고와야함

    _side_details = _food.side_detail(side_name)
    _side_nutrients = _food.side_nutrient(side_name)

    return (templates.TemplateResponse(
        "side-recipe.html",
        {"request": request,
         "side_name": side_name,
         "side_detail": _side_details,
         "side_nutrient": _side_nutrients}
    ))
    # return(templates.TemplateResponse
    #       ("side-recipe.html",
    #        {"request": request,
    #         "side_name": side_name,
    #         "side_ingredient": _side_details["ingredient"],
    #         "side_spice": _side_details["spice"],
    #         "side_recipe": _side_details["recipe"],
    #         "side_calorie": _side_nutrients["calorie"],
    #         "side_carbohydrate": _side_nutrients["carbohydrate"],
    #         "side_protein": _side_nutrients["protein"],
    #         "side_vitamin": _side_nutrients["vitamin"]}
    #        ))


@app.get("/soup/{soup_name}")
async def soup_recipe(request: Request, soup_name: str):
    # 클릭해서 들어간 soup_name에 해당하는 요소들을 갖고 와야함
    _soup_details = _food.soup_detail(soup_name)
    _soup_nutrients = _food.soup_nutrient(soup_name)

    return (templates.TemplateResponse(
        "soup-recipe.html",
        {"request": request,
         "soup_name": soup_name,
         "soup_detail": _soup_details,
         "soup_nutrient": _soup_nutrients}
    ))


@app.get("/diet")
async def diet(request: Request):
    _choice = FoodChoice(db_name, user, password, host, port)

    return (templates.TemplateResponse
            ("diet.html", {"request": request}))


@app.get("/add")
async def add(request: Request):
    return (templates.TemplateResponse
            ("add-food.html", {"request": request}))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# @app.post("/add")
# async def create(request: Request,
# food_type_id: str = Form(...), name: str= Form(...),
# ingredient: str= Form(...), spice: str= Form(...), recipe: str= Form(...),
# calorie: str= Form(...), carbohydrate: str= Form(...), protein: str= Form(...), vitamin: str= Form(...)):
