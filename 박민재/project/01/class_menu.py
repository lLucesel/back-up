from menu import *
from side_dish import *
from soup import *
menu_dict_1 = {1: print_gal,
               3: print_gogalby,
               5: print_cucumber_muchim,
               7: print_pork_neck,
               9: print_lettuce_kimchi,
               11: print_braised_tofu,
               13: print_braised_radish_with_mackerel}
menu_dict_2 = {2: print_JJagle,
               4: print_Perilla_Kimchi,
               6: print_Seaweed_Soup,
               8: print_Beef_Bone_Soup,
               10: print_Soybean_Sprout_Soup,
                  }
menu_dict = menu_dict_1.copy()
menu_dict.update(menu_dict_2)
class Recipe:
    def __init__(self, dinner, food):
        self._dinner = dinner
        self._food = food
        print_side_dish()
    def print_menu(self):
        if dinner == 3:
            print_side_dish()
            food = int(input("원하시는 반찬의 번호를 선택해주세요\n"))
            if food == 0:
                print(intro_menu)
            elif food in menu_dict_1:
                print(menu_dict_1[food]())
                print(return_menu)
            else:
                print(f"{failed_menu}\n{return_menu}")
    def print_side_menu(self):

    def print_soup(self):