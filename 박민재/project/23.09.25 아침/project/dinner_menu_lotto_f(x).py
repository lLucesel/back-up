from menu import *
from soup import *
from side_dish import *

print("""랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬/국 중 하나 고르기 : 3 / 4
저녁 메뉴 전체 레시피 보기 : 5
종료하기 : 6\n""")

# 무한 반복
while True:
    dinner = int(input(""))
    # 랜덤한 숫자 뽑아내기
    import random
    random_number_1 = random.randint(1, 9)
    random_number_2 = random.randint(1, 9)
    # 1 입력시 랜덤한 숫자 출력 후 문장 출력 및 12번줄로 돌아감
    if dinner == 1:
        print(f"{random_number_1}\n반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6")
    # 2 입력시 랜덤한 숫자 두개 출력 후 문장 출력 및 12번줄로 돌아감
    elif dinner == 2:
        print(f"( {random_number_1} / {random_number_2} )2\n반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6")
    # 3 입력시 메뉴판 출력
    elif dinner == 3:
        print_side_dish()
        food = int(input("원하시는 반찬의 번호를 선택해주세요\n"))
        if food == 0:
            print("""랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬/국 중 하나 고르기 : 3 / 4
저녁 메뉴 전체 레시피 보기 : 5
종료하기 : 6\n""")
        elif food == 1:
            print_gal()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 3:
            print_gogalby()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 5:
            print_cucumber_muchim()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 7:
            print_pork_neck()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 9:
            print_lettuce_kimchi()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 11:
            print_braised_tofu()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 13:
            print_braised_radish_with_mackerel()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        else:
            print("팔지 않는 메뉴입니다. 다시 입력해 주세요!\n")
    elif dinner == 4:
        print_soup()
        food = int(input("원하시는 국의 번호를 선택해주세요\n"))
        if food == 2:
            print_JJagle()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 4:
            print_Perilla_Kimchi()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 6:
            print_Seaweed_Soup()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 8:
            print_Beef_Bone_Soup()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 10:
            print_Soybean_Sprout_Soup()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        else:
            print("팔지 않는 메뉴입니다. 다시 입력해 주세요!\n")
    elif dinner == 5:
        print_menu()
        food = int(input("\n메뉴의 번호를 입력하세요!\n"))
        # 0 입력시 문장 출력 후 12번줄로 돌아감
        if food == 0:
            print("""랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬/국 중 하나 고르기 : 3 / 4
저녁 메뉴 전체 레시피 보기 : 5
종료하기 : 6\n""")
        # 1 입력시 1에 해당하는 레시피 출력 후 12번줄로 돌아감
        elif food == 1:
            print_gal()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 3:
            print_gogalby()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 5:
            print_cucumber_muchim()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 7:
            print_pork_neck()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 9:
            print_lettuce_kimchi()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 11:
            print_braised_tofu()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 13:
            print_braised_radish_with_mackerel()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")

        elif food == 2:
            print_JJagle()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 4:
            print_Perilla_Kimchi()
            print("반찬 복불복으로>> 1")
        elif food == 6:
            print_Seaweed_Soup()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 8:
            print_Beef_Bone_Soup()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        elif food == 10:
            print_Soybean_Sprout_Soup()
            print("반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n")
        # 메뉴판 이외의 숫자 입력 시 문장 출력 후 12번줄로 돌아감
        else:
            print("팔지 않는 메뉴입니다. 다시 입력해 주세요!\n")
    # 코드 종료
    else:
        print("장비를 정지합니다.")
        # 코드 이탈
        break
#class / try / exception / raise 찾아보기
#except InvalidMenuException as e:
#print("잘못된 메뉴!")
#mvc 공부해보기