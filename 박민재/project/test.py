import random
from menu import *
from side_dish import *
from soup import *

class DinnerMenu:
    def __init__(self):
        self.menu_diction_1 = {
            1: print_gal,
            3: print_gogalby,
            5: print_cucumber_muchim,
            7: print_pork_neck,
            9: print_lettuce_kimchi,
            11: print_braised_tofu,
            13: print_braised_radish_with_mackerel}

        self.menu_diction_2 = {
            2: print_JJagle,
            4: print_Perilla_Kimchi,
            6: print_Seaweed_Soup,
            8: print_Beef_Bone_Soup,
            10: print_Soybean_Sprout_Soup}

        self.menu_diction = {**self.menu_diction_1, **self.menu_diction_2}
        self.introduction_menu = """랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬/국 중 하나 고르기 : 3 / 4
저녁 메뉴 전체 레시피 보기 : 5
종료하기 : 6\n"""
        self.return_menu = "반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n"
        self.failed_menu = "팔지 않는 메뉴입니다. 다시 입력해 주세요!\n"

    def choose_random_dish(self, count):
        random_numbers = [random.randint(1, 9) for _ in range(count)]
        return ' / '.join(str(num) for num in random_numbers)

    def print_menu(self, menu_type):
        if menu_type == 1:
            for number, recipe_func in self.menu_diction_1.items():
                print(f"{number}: {recipe_func}")
        elif menu_type == 2:
            for number, recipe_func in self.menu_diction_2.items():
                print(f"{number}: {recipe_func}")
        else:
            for number, recipe_func in self.menu_diction.items():
                print(f"{number}: {recipe_func}")

    def run(self):
        while True:
            print(self.introduction_menu)
            dinner = int(input("메뉴를 선택하세요: "))

            if dinner == 1:
                random_number = random.randint(1, 9)
                print(f"{random_number}\n{self.return_menu}")
            elif dinner == 2:
                random_numbers = self.choose_random_dish(2)
                print(f"( {random_numbers} )\n{self.return_menu}")
            elif 3 <= dinner <= 4:
                menu_type = 1 if dinner == 3 else 2
                self.print_menu(menu_type)
                food = int(input("원하시는 메뉴의 번호를 선택해주세요: "))
                menu_dict = self.menu_diction_1 if menu_type == 1 else self.menu_diction_2
                if food in menu_dict:
                    print(f"{menu_dict[food]}()\n{self.return_menu}")
                else:
                    print(f"{self.failed_menu}\n{self.return_menu}")
            elif dinner == 5:
                self.print_menu(0)
                food = int(input("\n메뉴의 번호를 입력하세요: "))
                if food in self.menu_diction:
                    print(f"{self.menu_diction[food]}()\n{self.return_menu}")
                else:
                    print(f"{self.failed_menu}\n{self.return_menu}")
            elif dinner == 6:
                print("장비를 정지합니다.")
                break


if __name__ == '__main__':
    app = DinnerMenu()
    app.run()