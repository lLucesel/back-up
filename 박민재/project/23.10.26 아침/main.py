import random
from fastapi import FastAPI, Request, Form
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



@app.get("/")
async def main(request: Request):
    _food_choice = FoodChoice(db_name, user, password, host, port)

    ran_side_name = _food_choice.ran_side()
    ran_soup_name = _food_choice.ran_soup()

    _food_choice.close_connection()
    return (templates.TemplateResponse
            ("main.html", {"request": request, "side_name": ran_side_name, "soup_name": ran_soup_name}))


@app.get("/side")
async def side(request: Request):
    _food = FoodDetail(db_name, user, password, host, port)

    side_name = _food.side_name
    side_name = sorted(side_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("side.html", {"request": request, "side_name": side_name}))


@app.get("/soup")
async def soup(request: Request):
    _food = FoodDetail(db_name, user, password, host, port)

    soup_name = _food.soup_name
    soup_name = sorted(soup_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("soup.html", {"request": request, "soup_name": soup_name}))


@app.get("/side/{side_name}")
async def side_recipe(request: Request, side_name: str):
    _food = FoodDetail(db_name, user, password, host, port)
# 클릭해서 들어간 side_name에 해당하는 요소들을 갖고와야함
    _side_ingredient = _food.side_detail["ingredient"]
    _side_spice = _food.side_detail["spice"]
    _side_recipe = _food.side_detail["recipe"]
    _side_calorie = _food.side_nutrient["calorie"]
    _side_carbohydrate = _food.side_nutrient["carbohydrate"]
    _side_protein = _food.side_nutrient["protein"]
    _side_vitamin = _food.side_nutrient["vitamin"]

    return (templates.TemplateResponse
            ("side-recipe.html",
             {"request": request,
              "side_name": side_name,
              "side_ingredient": _side_ingredient,
              "side_spice": _side_spice,
              "side_recipe": _side_recipe,
              "side_calorie": _side_calorie,
              "side_carbohydrate": _side_carbohydrate,
              "side_protein": _side_protein,
              "side_vitamin": _side_vitamin
              }))


@app.get("/soup/{soup_name}")
async def soup_recipe(request: Request, soup_name: str):
    _food = FoodDetail(db_name, user, password, host, port)

    _soup_ingredient = _food.soup_detail["ingredient"]
    _soup_spice = _food.soup_detail["spice"]
    _soup_recipe = _food.soup_detail["recipe"]
    _soup_calorie = _food.soup_nutrient["calorie"]
    _soup_carbohydrate = _food.soup_nutrient["carbohydrate"]
    _soup_protein = _food.soup_nutrient["protein"]
    _soup_vitamin = _food.soup_nutrient["vitamin"]

    return (templates.TemplateResponse
            ("soup-recipe.html",
             {"request": request,
              "soup_name": soup_name,
              "soup_ingredient": _soup_ingredient,
              "soup_spice": _soup_spice,
              "soup_recipe": _soup_recipe,
              "soup_calorie": _soup_calorie,
              "soup_carbohydrate": _soup_carbohydrate,
              "soup_protein": _soup_protein,
              "soup_vitamin": _soup_vitamin
              }))


@app.get("/diet")
async def diet(request: Request):
    #_choice = FoodChoice(db_name, user, password, host, port)
    #_man_calorie = _choice.man_calorie
    #_woman_calorie = _choice.woman_calorie
    return (templates.TemplateResponse
            ("diet1.html", {"request": request}))


@app.get("/add")
async def add(request: Request):
    return (templates.TemplateResponse
            ("add-food.html", {"request": request}))


# @app.post("/add")
# async def create(request: Request,
# food_type_id: str = Form(...), name: str= Form(...),
# ingredient: str= Form(...), spice: str= Form(...), recipe: str= Form(...),
# calorie: str= Form(...), carbohydrate: str= Form(...), protein: str= Form(...), vitamin: str= Form(...)):
#
#


# async def create_todo(request: Request, title: str = Form(...), description: str = Form(...),
#                      priority: int = Form(...), db: Session = Depends(get_db)):
#    user = await get_current_user(request)
#    if user is None:
#        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
#
#    todo_model = models.Todos()
#    todo_model.title = title
#    todo_model.description = description
#    todo_model.priority = priority
#    todo_model.complete = False
#    todo_model.owner_id = user.get("id")
#
#    db.add(todo_model)
#    db.flush()
#    db.commit()
#
#    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)
