import random
import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from choice import FoodChoice
from detail import FoodDetail
from database import MySQLClientConnector
from diet import FoodDiet

app = FastAPI()
templates = Jinja2Templates(directory="templates")

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

_add = MySQLClientConnector(db_name, user, password, host, port)
_food_choice = FoodChoice(db_name, user, password, host, port)
_food_detail = FoodDetail(db_name, user, password, host, port)
_food_diet = FoodDiet(db_name, user, password, host, port)


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
    _side_name = _food_detail.side_name()
    _side_name = sorted(_side_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("side.html", {"request": request, "side_name": _side_name}))


@app.get("/soup")
async def soup(request: Request):
    _soup_name = _food_detail.soup_name()
    _soup_name = sorted(_soup_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("soup.html", {"request": request, "soup_name": _soup_name}))


@app.get("/side/{side_name}")
async def side_recipe(request: Request, side_name: str):
    # 클릭해서 들어간 side_name에 해당하는 요소들을 갖고와야함

    _side_details = _food_detail.side_detail(side_name)
    _side_nutrients = _food_detail.side_nutrient(side_name)

    return (templates.TemplateResponse(
        "side-recipe.html",
        {"request": request,
         "side_name": side_name,
         "side_detail": _side_details,
         "side_nutrient": _side_nutrients}
    ))


# @app.post("/side/{side_name}")
# async def add_new(request: Request,
#                  side_name: str,
#                  new_name: str = Form(...),
#                  new_ingredient: str = Form(...),
#                  new_spice: str = Form(...),
#                  new_recipe: str = Form(...),
#                  new_calorie: str = Form(...),
#                  new_carbohydrate: str = Form(...),
#                  new_protein: str = Form(...),
#                  new_vitamin: str = Form(...),
#                  ):
#    _side_details = _food_detail.side_detail(side_name)
#    _side_nutrients = _food_detail.side_nutrient(side_name)
#
#    if not _side_details and not _side_nutrients:
#        raise HTTPException(status_code=404, detail="Side menu not found")
#
#    _side_details.name = new_name
#    _side_details.ingredient = new_ingredient
#    _side_details.spice = new_spice
#    _side_details.recipe = new_recipe
#    _side_nutrients.carbohydrate = new_carbohydrate
#    _side_nutrients.calorie = new_calorie
#    _side_nutrients.protein = new_protein
#    _side_nutrients.vitamin = new_vitamin
#
#
#    return RedirectResponse(url="/side/{side_name}", status_code=status.HTTP_302_FOUND)


@app.get("/soup/{soup_name}")
async def soup_recipe(request: Request, soup_name: str):
    # 클릭해서 들어간 soup_name에 해당하는 요소들을 갖고 와야함
    _soup_details = _food_detail.soup_detail(soup_name)
    _soup_nutrients = _food_detail.soup_nutrient(soup_name)

    return (templates.TemplateResponse(
        "soup-recipe.html",
        {"request": request,
         "soup_name": soup_name,
         "soup_detail": _soup_details,
         "soup_nutrient": _soup_nutrients}
    ))


# @app.get("/diet")
# async def diet(request: Request):
#    return (templates.TemplateResponse
#            ("_diet.html", {"request": request}))
@app.get("/diet")
async def diet(request: Request):
    _diet = _food_diet.diet_plan()

    sun_side_cal = _diet[0][0]["calorie"] + _diet[0][1]["calorie"] + _diet[0][2]["calorie"]
    mon_side_cal = _diet[1][0]["calorie"] + _diet[1][1]["calorie"] + _diet[1][2]["calorie"]
    tue_side_cal = _diet[2][0]["calorie"] + _diet[2][1]["calorie"] + _diet[2][2]["calorie"]
    wed_side_cal = _diet[3][0]["calorie"] + _diet[3][1]["calorie"] + _diet[3][2]["calorie"]
    thu_side_cal = _diet[4][0]["calorie"] + _diet[4][1]["calorie"] + _diet[4][2]["calorie"]
    fri_side_cal = _diet[5][0]["calorie"] + _diet[5][1]["calorie"] + _diet[5][2]["calorie"]
    sat_side_cal = _diet[6][0]["calorie"] + _diet[6][1]["calorie"] + _diet[6][2]["calorie"]

    sun_soup_cal = _diet[0][3]["calorie"]
    mon_soup_cal = _diet[1][3]["calorie"]
    tue_soup_cal = _diet[2][3]["calorie"]
    wed_soup_cal = _diet[3][3]["calorie"]
    thu_soup_cal = _diet[4][3]["calorie"]
    fri_soup_cal = _diet[5][3]["calorie"]
    sat_soup_cal = _diet[6][3]["calorie"]

    sun_cal = sun_side_cal + sun_soup_cal
    mon_cal = mon_side_cal + mon_soup_cal
    tue_cal = tue_side_cal + tue_soup_cal
    wed_cal = wed_side_cal + wed_soup_cal
    thu_cal = thu_side_cal + thu_soup_cal
    fri_cal = fri_side_cal + fri_soup_cal
    sat_cal = sat_side_cal + sat_soup_cal

    all_side = sun_side_cal + mon_side_cal + tue_side_cal + wed_side_cal + thu_side_cal + fri_side_cal + sat_side_cal
    all_soup = sun_soup_cal + mon_soup_cal + tue_soup_cal + wed_soup_cal + thu_soup_cal + fri_soup_cal + sat_soup_cal
    all_food = all_side + all_soup

    sun_car = (_diet[0][0]["carbohydrate"] + _diet[0][1]["carbohydrate"] +
               _diet[0][2]["carbohydrate"] + _diet[0][3]["carbohydrate"])
    mon_car = (_diet[1][0]["carbohydrate"] + _diet[1][1]["carbohydrate"] +
               _diet[1][2]["carbohydrate"] + _diet[1][3]["carbohydrate"])
    tue_car = (_diet[2][0]["carbohydrate"] + _diet[2][1]["carbohydrate"] +
               _diet[2][2]["carbohydrate"] + _diet[2][3]["carbohydrate"])
    wed_car = (_diet[3][0]["carbohydrate"] + _diet[3][1]["carbohydrate"] +
               _diet[3][2]["carbohydrate"] + _diet[3][3]["carbohydrate"])
    thu_car = (_diet[4][0]["carbohydrate"] + _diet[4][1]["carbohydrate"] +
               _diet[4][2]["carbohydrate"] + _diet[4][3]["carbohydrate"])
    fri_car = (_diet[5][0]["carbohydrate"] + _diet[5][1]["carbohydrate"] +
               _diet[5][2]["carbohydrate"] + _diet[5][3]["carbohydrate"])
    sat_car = (_diet[6][0]["carbohydrate"] + _diet[6][1]["carbohydrate"] +
               _diet[6][2]["carbohydrate"] + _diet[6][3]["carbohydrate"])
    all_car = sun_car + mon_car + tue_car + wed_car + thu_car + fri_car + sat_car

    sun_pro = (_diet[0][0]["protein"] + _diet[0][1]["protein"] +
               _diet[0][2]["protein"] + _diet[0][3]["protein"])
    mon_pro = (_diet[1][0]["protein"] + _diet[1][1]["protein"] +
               _diet[1][2]["protein"] + _diet[1][3]["protein"])
    tue_pro = (_diet[2][0]["protein"] + _diet[2][1]["protein"] +
               _diet[2][2]["protein"] + _diet[2][3]["protein"])
    wed_pro = (_diet[3][0]["protein"] + _diet[3][1]["protein"] +
               _diet[3][2]["protein"] + _diet[3][3]["protein"])
    thu_pro = (_diet[4][0]["protein"] + _diet[4][1]["protein"] +
               _diet[4][2]["protein"] + _diet[4][3]["protein"])
    fri_pro = (_diet[5][0]["protein"] + _diet[5][1]["protein"] +
               _diet[5][2]["protein"] + _diet[5][3]["protein"])
    sat_pro = (_diet[6][0]["protein"] + _diet[6][1]["protein"] +
               _diet[6][2]["protein"] + _diet[6][3]["protein"])
    all_pro = sun_pro + mon_pro + tue_pro + wed_pro + thu_pro + fri_pro + sat_pro

    sun_vit = (_diet[0][0]["vitamin"] + _diet[0][1]["vitamin"] +
               _diet[0][2]["vitamin"] + _diet[0][3]["vitamin"])
    mon_vit = (_diet[1][0]["vitamin"] + _diet[1][1]["vitamin"] +
               _diet[1][2]["vitamin"] + _diet[1][3]["vitamin"])
    tue_vit = (_diet[2][0]["vitamin"] + _diet[2][1]["vitamin"] +
               _diet[2][2]["vitamin"] + _diet[2][3]["vitamin"])
    wed_vit = (_diet[3][0]["vitamin"] + _diet[3][1]["vitamin"] +
               _diet[3][2]["vitamin"] + _diet[3][3]["vitamin"])
    thu_vit = (_diet[4][0]["vitamin"] + _diet[4][1]["vitamin"] +
               _diet[4][2]["vitamin"] + _diet[4][3]["vitamin"])
    fri_vit = (_diet[5][0]["vitamin"] + _diet[5][1]["vitamin"] +
               _diet[5][2]["vitamin"] + _diet[5][3]["vitamin"])
    sat_vit = (_diet[6][0]["vitamin"] + _diet[6][1]["vitamin"] +
               _diet[6][2]["vitamin"] + _diet[6][3]["vitamin"])
    all_vit = sun_vit + mon_vit + tue_vit + wed_vit + thu_vit + fri_vit + sat_vit

    #_add.close()
    return (templates.TemplateResponse
            ("diet.html", {"request": request,
                           "_diet": _diet, "all_soup": all_soup,
                           "sun_cal": sun_cal, "mon_cal": mon_cal, "tue_cal": tue_cal, "wed_cal": wed_cal,
                           "thu_cal": thu_cal, "fri_cal": fri_cal, "sat_cal": sat_cal, "all_cal": all_food,
                           "sun_car": sun_car, "mon_car": mon_car, "tue_car": tue_car, "wed_car": wed_car,
                           "thu_car": thu_car, "fri_car": fri_car, "sat_car": sat_car, "all_car": all_car,
                           "sun_pro": sun_pro, "mon_pro": mon_pro, "tue_pro": tue_pro, "wed_pro": wed_pro,
                           "thu_pro": thu_pro, "fri_pro": fri_pro, "sat_pro": sat_pro, "all_pro": all_pro,
                           "sun_vit": sun_vit, "mon_vit": mon_vit, "tue_vit": tue_vit, "wed_vit": wed_vit,
                           "thu_vit": thu_vit, "fri_vit": fri_vit, "sat_vit": sat_vit, "all_vit": all_vit
                           }))


@app.get("/add")
async def add(request: Request):
    return (templates.TemplateResponse
            ("add-food.html", {"request": request}))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# @app.post("/add")
# async def create(request: Request,
# food_type_id: int = Form(...), name: str= Form(...),
# ingredient: str= Form(...), spice: str= Form(...), recipe: str= Form(...),
# calorie: str= Form(...), carbohydrate: str= Form(...), protein: str= Form(...), vitamin: str= Form(...)):
