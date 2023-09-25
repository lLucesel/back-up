import templates
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from menu import *
from soup import *
from side_dish import *

intro_menu = """랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬/국 중 하나 고르기 : 3 / 4
저녁 메뉴 전체 레시피 보기 : 5
식단짜기 : 6
종료하기 : 7\n"""
return_menu = "반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    식단짜기 >> 6   종료하기 >> 7"
failed_menu = "팔지 않는 메뉴입니다. 다시 입력해 주세요!"
error_message = "맞지 않은 번호입니다! 다시 입력해 주세요!"
menu_dict_1 = {
    1: print_gal,
    3: print_gogalby,
    5: print_cucumber_muchim,
    7: print_pork_neck,
    9: print_lettuce_kimchi,
    11: print_braised_tofu,
    13: print_braised_radish_with_mackerel
}
menu_dict_2 = {
    2: print_JJagle,
    4: print_Perilla_Kimchi,
    6: print_Seaweed_Soup,
    8: print_Beef_Bone_Soup,
    10: print_Soybean_Sprout_Soup
}
menu_dict = menu_dict_1.copy()
menu_dict.update(menu_dict_2)

# 여기에 메뉴 함수와 상수를 정의합니다.

app = FastAPI()

# 정적 파일 (HTML, CSS, JavaScript) 제공
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>랜덤 저녁 메뉴 선택기</title>
    </head>
    <body>
        <h1>랜덤 저녁 메뉴 선택기에 오신 것을 환영합니다</h1>
        <p>옵션을 선택하세요:</p>
        <ul>
            <li><a href="/random_dinner">랜덤 저녁 메뉴 (1 또는 2 개 항목)</a></li>
            <li><a href="/side_dish">반찬 선택하기</a></li>
            <li><a href="/soup">국 선택하기</a></li>
            <li><a href="/all_menus">모든 메뉴 보기</a></li>
            <li><a href="/create_menu">사용자 지정 메뉴 생성</a></li>
        </ul>
    </body>
    </html>
    """


app = FastAPI()


@app.get("/random_dinner", response_class=HTMLResponse)
async def random_dinner():
    print(intro_menu)
    while True:
        try:
            dinner = int(input(""))
            import random

            random_number_1 = random.randint(1, 9)
            random_number_2 = random.randint(1, 9)
            if dinner == 1:
                print(f"{random_number_1}\n{return_menu}")
            elif dinner == 2:
                print(f"( {random_number_1} / {random_number_2} )\n{return_menu}")
            elif dinner == 3:
                print_side_dish()
                food = int(input("원하시는 반찬의 번호를 선택해주세요\n"))
                if food == 0:
                    print(intro_menu)
                elif food in menu_dict_1:
                    menu_dict_1[food]()
                    print(return_menu)
                else:
                    print(failed_menu + "\n" + return_menu)
            elif dinner == 4:
                print_soup()
                food = int(input("원하시는 국의 번호를 선택해주세요\n"))
                if food == 0:
                    print(intro_menu)
                elif food in menu_dict_2:
                    menu_dict_2[food]()
                    print(return_menu)
                else:
                    print(failed_menu + "\n" + return_menu)
            elif dinner == 5:
                print_menu()
                food = int(input("\n메뉴의 번호를 입력하세요!\n"))
                if food == 0:
                    print(intro_menu)
                elif food in menu_dict:
                    menu_dict[food]()
                    print(return_menu)
                else:
                    print(failed_menu + "\n" + return_menu)
            elif dinner == 6:
                list_a = [512, 356, 477, 611, 532, 453, 499, 378, 561, 444, 531, 601, 387, 426, 468]
                list_b = [95, 142, 111, 132, 128, 89, 121, 99, 104, 71, 101, 130, 95, 108, 102]

                result_a = []
                result_b = []
                total_sum = 0

                while True:
                    if len(result_a) == 7 and len(result_b) == 7:
                        break
                    selected_list = random.choice([list_a, list_b])
                    selected_number = random.choice(selected_list)
                    if selected_list is list_a and len(result_a) < 7 and total_sum + selected_number <= 5000:
                        result_a.append(selected_number)
                        total_sum += selected_number
                    elif selected_list is list_b and len(result_b) < 7 and total_sum + selected_number <= 5000:
                        result_b.append(selected_number)
                        total_sum += selected_number
                print("랜덤하게 선택된 반찬의 칼로리:", result_a)
                print("랜덤하게 선택된 국의 칼로리:", result_b)
                print("반찬 칼로리의 총합:", sum(result_a))
                print("국 칼로리의 총합:", sum(result_b))
                print("총합:", total_sum)
                print(return_menu)
            elif dinner == 7:  # 6 입력시 종료
                print("장비를 정지합니다.")
                break
            else:
                if dinner >= 8:  # 7 이상의 숫자 입력시 에러 출력 후 되돌아가기
                    raise ValueError(error_message + "\n" + return_menu)
                print(error_message + "\n" + return_menu)
        except ValueError:
            print(error_message + "\n" + return_menu)
    return templates.TemplateResponse("dineer_html_main.html",
                                      {"request": request, "intro_menu": intro_menu, "return_menu": return_menu})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
