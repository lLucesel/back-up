from fastapi import FastAPI


def print_menu():
    print("""MENU\n
밥                       국
<1> 갈배제육              <2> 돼지김치짜글이
<3> 고등어 갈비구이        <4> 들깨배춧국
<5> 오이부추무침           <6> 미역국
<7> 돼지목살 간장구이       <8> 소고기 뭇국
<9> 상추 겉절이           <10> 콩나물 국
<11> 두부조림
<13> 무 고등어 조림   
<15> 

<0> 처음으로""")


def print_side_dish():
    print("""밥
<1> 갈배제육
<3> 고등어 갈비구이
<5> 오이부추무침
<7> 돼지목살 간장구이
<9> 상추 겉절이
<11> 두부조림
<13> 무 고등어 조림
<15> 

<0> 처음으로\n""")


def print_soup():
    print("""국
<2> 돼지김치짜글이
<4> 들깨배춧국
<6> 미역국
<8> 소고기 뭇국
<10> 콩나물국

<0> 처음으로\n""")

def print_JJagle():
    print("""<2> 돼지김치짜글이\n
주재료                   양념
1. 앞다리 살              1. 들기름 반스푼
2. 신김치 반포기 이하       2. 올리브유 반스푼
3. 대파                  3. 고추장 한스푼
4. 양파 반개              4. 고춧가루 한스푼
                        5. 다진 마늘 한스푼
                        6. 간장 한스푼
                        7. 설탕 한스푼
                        8. 맛술 반스푼
                        9. 후추 살짝\n
만드는 법
1. 앞다리 살에 맛술과 후추를 뿌려 30분가량 상온에 놔둔다
1-1. 위 과정은 고기의 잡내를 잡기 위함이며 하지 않아도 상관없다
2. 냄비에 들기름 반, 올리브유 반을 부은 후 파와 함께 살짝 볶으며 파기름을 내준다
3. 고기를 넣어 중불로 2,3분 가량 볶아준다
3-1. 이때 고기를 재지 않았으면 맛술 반스푼과 후추를 살짝 뿌려준다
4. 고추장 한스푼, 고춧가루 한스푼, 다진 마늘 한스푼, 설탕 한스푼, 간장 한스푼을 넣어 중불로 2분가량 볶아준다
4-1. 위의 양념은 자신의 입맛에 따라 가감한다
5. 얇게 썬 김치와 양파를 넣어 같이 볶아준다
5-1. 이때 김치를 그냥 썰어 넣으면 김치의 속과 김치 국물에 의해 너무 짜질 수 있으니 칼로 속을 긁어내고 김치를 어느 정도 짜준다.
6. 양파가 반투명하게 변하면 물을 700ml 가량 넣어준다
7. 강불로 끓이며 적당히 졸인다\n""")


def print_Perilla_Kimchi():
    print("""<4> 들깨 배춧국\n
주재료                 양념
1. 무 200g            1. 다진 마늘 한스푼
2. 배추 3장            2. 국간장 1.5스푼
3. 다진 파 한스푼       3. 소금 한스푼
                      4. 들깨가루 세스푼\n
만드는 법
1. 무를 썰어준다.
1-1. 이때 나박썰기를 해도 되고 일반 뭇국 끓이듯이 네모 얇게 썰어도 된다.
2. 육수를 우려준다.
2-1. 이때 육수를 우려주지 않아도 된다.
3. 무와 배추를 넣어 맛을 우려준다.
4. 어느 정도 무가 투명해지면 들깨가루를 제외한 양념을 넣고 끓여준다.
4-1. 국간장은 멸치 액젓으로 대체 가능하고 액젓과 소금은 입맛에 따라 가감한다. 소금은 나중에 넣어서 간을 맞춰도 된다.
5. 마지막에 들깨가루를 넣어 5분간 끓여준다.
5-1. 들깨가루의 양은 알아서 가감하기\n""")


def print_Seaweed_Soup():
    print("""<6> 미역국\n
주재료                     양념
1. 미역 2숟가락(5g)         1. 들기름 한스푼
2. 소고기 국거리용 50g       2. 국간장 1.5스푼
3. 물 600ml               3. 액젓 반스푼
                          4. 다진마늘 반스푼\n
만드는 법
1. 미역을 물에 넣고 10분에서 20분간 불려준다.
2. 냄비에 들기름 한스푼을 붓고 다진마늘과 함께 소고기를 살짝 볶아준다.
3. 불린 미역을 짠 후 국간장과 함께 볶은 소고기와 같이 볶아준다.
4. 5분에서 10분간 볶은 후 물을 부어준다.
5. 물을 붓고 액젓을 넣어준 후 끓인다.
5-1. 이때 액젓은 까나리, 멸치 등등 상관없다.
6. 계속 끓이면서 액젓이나 소금으로 간을 맞춘다.\n""")


def print_Beef_Bone_Soup():
    print("""<8> 소고기 뭇국\n
주재료                 양념
1. 소고기 300g         1. 국간장 두스푼
2. 무 400g            2. 멸치 액젓 한스푼
3. 대파 20cm           3. 다진 마늘 한스푼
                      4. 멸치 다시마 육수 1200ml
                      5. 후추 살짝\n
만드는 법
1. 무를 나박하게 썰어준다.
2. 냄비에 소고기를 넣고 국간장과 액젓, 다진 마늘과 후추를 넣어 볶아준다.
3. 고기 색깔이 어느정도 변하면 무를 넣고 같이 5분가량 볶아준다.
4. 육수를 붓고 끓여준다.
5. 강불로 5분가량 끓여준 후 대파를 넣어 끓여준다.\n""")


def print_Soybean_Sprout_Soup():
    print("""<10> 콩나물 국\n
주재료                 양념
1. 콩나물 200g         1. 청양고추 소량
2. 황태채 한줌          2. 다진 마늘 반스푼
3. 대파 15cm           3. 액젓 1.5스푼
                      4. 소금 약간
                      5. 육수 1200ml\n
만드는 법
1. 파는 어슷썰고 북어채는 흐르는 물에 가볍게 씻어준다.
2. 육수에 황태채를 넣고 끓여준다.
3. 이때 센불로 끓이다가 물이 끓으면, 중불로 4분간 끓인 후 잠시 불을 꺼준다.
3-1. 3분에서 4분간 불을 꺼주는데 이때 거품을 걷어주면 맑은 국물이 나온다.
4. 액젓과 다진 마늘을 넣고 강불로 물이 끓으면 콩나물과 대파를 넣어준다.
4-1. 이때 뚜껑을 완전 열거나 완전 닫아야 비린내가 나지 않는다.
5. 부족한 간은 소금으로 맞추고 청양 고추를 넣어주면 칼칼해진다.\n""")


def print_gal():
    print("""<1> 갈배제육 만들기\n
주재료                          양념     
돼지고기 앞다리 살 600그램         고추장 듬뿍 세 숟갈
어슷 썬 대파                     간장 두 숟갈
양파 반개                        설탕 두 숟갈
소금 한 꼬집                     배 음료 한 캔
                               다진 마늘 한 숟갈 

                               식초 두 숟갈
                               참기름 한 숟갈\n
만드는 법
1. 고기의 핏물을 닦아 준다.
2. 고추장에서 다진 마늘까지의 양념을 잘 섞어준다.
3. 양념과 고기를 잘 섞어준 후 식초와 참기름을 넣어준다.(식초는 연육 적용과 감칠맛을 올려주고 보관 기간을 늘려주며 고기를 신맛은 볶을때 사라진다.)
4. 어슷 썬 채소들은 고기 위에 올려주고(섞기X) 소금 한 꼬집을 뿌려준다.\n
굽는 법
1. 고기를 먼저 올려 거뭇한 부분이 생길때까지 기다린다.(거뭇한 부위는 감칠맛을 올려줌)
2. 어느 정도 거뭇한 분이 생기면 채소들을 넣어 같이 볶아준 후 뚜껑을 덮고 약불로 3분을 익혀준다.
3. 마무리로 으깬 마늘을 한 숟갈 넣어 섞어주고 후추를 뿌려준다.\n""")


def print_gogalby():
    print("""<3> 고등어 갈비구이 만들기\n
주재료                   양념
1. 고등어 한마리          1. 밀가루
2. 다진 파 반움큼         2. 맛술

                        3. 고추장 한스푼
                        4. 고춧가루 한스푼
                        5. 다진 마늘 반스푼
                        6. 간장 반스푼
                        7. 들기름 한스푼
                        8. 설탕 반스푼
                        9. 올리고당 한스푼
                        10. 맛술 한스푼
                        11. 후추 살짝
                        12. 깨 적당히\n
만드는 법
1. 고등어를 물에 담근 후 맛술 한스푼, 후추 살짝, 밀가루 적당량을 넣어 비린내를 제거한다. 대략 30분
2. 양념들과 다진 파를 잘 섞어준다.
2-1. 여기서 양념은 자기 입맛에 따라 조절한다. 자반 고등어일 경우 간장은 한스푼이 아닌 살짝만 넣어도 된다.
3. 비린내를 제거한 고등어에 밀가루를 뿌리고 고등어를 굽는다.
3-1. 밀가루를 입혀주면 기름이 잘 튀지 않는다.
4. 앞뒤로 5~10분정도 구운 후 양념을 위에 골고루 발라준다.
5. 불을 약불로 줄이거나 완전히 끈 후 뚜껑을 덮어 3분가량 익혀준다.
5-1. 불을 끈 후 고등어를 뒤집어 반대편에도 양념을 발라준다. 굽는건 자기가 알아서 적당히.\n""")


def print_cucumber_muchim():
    print("""<4> 오이부추무침 만들기\n
주재료             양념
1. 오이 3개        1. 고춧가루 3큰술
2. 부추 한줌        2. 다진 마늘 반큰술
                  3. 액젓 1큰술
                  4.매실액 1큰술
                  5. 설탕 조금
                  6. 맛술 1큰술
                  7. 통깨 적당히\n
만드는 법
1. 부추와 오이를 씻은 후 오이는 길게 네토막 내준다.
1-1. 이때 오이는 굵은 소금으로 문질러서 씻어줘도 된다.
2. 굵은 소금을 한큰술 안되게 뿌려서 재워둔다.
3. 통깨를 제외한 위의 양념들을 섞어준다.
3-1. 이때 액젓과 매실액은 입맛에 따라 가감하고 오이와 고춧가루가 1:1 비례하게 넣어준다. 물론 고춧가루 또한 입맛에 따라 알아서 가감
4. 절여놨던 오이를 헹구고 물기를 빼 체에 받쳐준다.
4-1. 물기를 너무 빼면 무칠 때 굉장히 퍽퍽해지니 적당히 뺄 것.
5. 양념과 오이를 버무려주며 깨를 적당량 뿌려준다.\n""")


def print_pork_neck():
    print("""<7> 돼지목살간장구이 만들기""")


def print_lettuce_kimchi():
    print("""<9> 상추 겉절이 만들기""")


def print_braised_tofu():
    print("""<11> 두부조림 만들기""")


def print_braised_radish_with_mackerel():
    print("""<13> 무 고등어 조림 만들기""")

intro_menu = """랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬 고르기 : 3
국 고르기 : 4
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
print(intro_menu)

app = FastAPI()

while True:  # 무한 반복(현업에선 거의 안 씀. 메모리 뻑나서)
    try:
        dinner = int(input(""))
        import random  # 랜덤한 숫자 뽑아내기

        random_number_1 = random.randint(1, 9)
        random_number_2 = random.randint(1, 9)
        if dinner == 1:  # 1 입력시 랜덤한 숫자 출력 후 문장 출력 및 처음으로 돌아감
            print(f"{random_number_1}\n{return_menu}")
        elif dinner == 2:  # 2 입력시 랜덤한 숫자 두개 출력 후 문장 출력 및 처음으로 돌아감
            print(f"( {random_number_1} / {random_number_2} )\n{return_menu}")
        elif dinner == 3:  # 3 입력시 반찬 메뉴판 출력
            print_side_dish()
            food = int(input("원하시는 반찬의 번호를 선택해주세요\n"))
            if food == 0:  # 처음 안내판 출력
                print(intro_menu)
            elif food in menu_dict_1:  # 출력한 메뉴판에서 원하는 음식에 해당하는 번호 입력 시 해당 레시피 출력
                menu_dict_1[food]()
                print(return_menu)
            else:  # 메뉴판 이외의 숫자 입력 시 문장 출력 후 26번줄로 돌아감
                print(failed_menu + "\n" + return_menu)
        elif dinner == 4:  # 4 입력시 국 메뉴판 출력
            print_soup()
            food = int(input("원하시는 국의 번호를 선택해주세요\n"))
            if food == 0:  # 처음 안내판 출력
                print(intro_menu)
            elif food in menu_dict_2:  # 출력한 메뉴판에서 우너하는 음식에 해당하는 번호 입력 시 해당 레시피 출력
                menu_dict_2[food]()
                print(return_menu)
            else:  # 메뉴판 이외의 숫자 입력 시 문장 출력 후 26번줄로 돌아감
                print(failed_menu + "\n" + return_menu)
        elif dinner == 5:  # 5 입력시 전체 메뉴판 출력
            print_menu()
            food = int(input("\n메뉴의 번호를 입력하세요!\n"))
            if food == 0:  # 0 입력시 intro_menu 호출 후 26번줄로 돌아감
                print(intro_menu)
            elif food in menu_dict:  # 1 입력 후 숫자에 해당하는 레시피 출력 후 26번줄로 돌아감
                menu_dict[food]()
                print(return_menu)
            else:  # 메뉴판 이외의 숫자 입력 시 문장 출력 후 26번줄로 돌아감
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

# if/elif 구조를 try로 바꾸기
# class 선언으로 간소하하기 def 메뉴, 밥, 국
# 콜백과 1급함수 공부해서 메모리 주소 나오는거 고치기
# 디버깅툴로 코드 흐름 따라가기
