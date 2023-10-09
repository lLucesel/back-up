import random


def random_menu_two():
    random_number_1 = random.randint(1, 9)
    random_number_2 = random.randint(1, 9)
    print(f"( {random_number_1} / {random_number_2} )")


def random_menu_one():
    random_number_1 = random.randint(1, 9)
    return random_number_1


class DinnerLotto:
    def __init__(self):
        self.intro_menu = """
반찬 고르기 : 3
국 고르기 : 4
종료하기 : 7\n"""
        self.return_menu = "반찬 고르기 >> 3    국 고르기 >> 4   종료하기 >> 7"
        self.failed_menu = "팔지 않는 메뉴입니다. 다시 입력해 주세요!"
        self.error_message = "맞지 않은 번호입니다! 다시 입력해 주세요!"

    def print_intro_menu(self):
        return self.intro_menu

    def print_return_menu(self):
        return self.return_menu

    def print_failed_menu(self):
        return self.failed_menu + "\n" + self.return_menu

    def print_error_message(self):
        return self.error_message + "\n" + self.return_menu

    def select_side(self):
        try:
            dinner = int(input(""))
            if dinner == 3:
                print_side_dish()
                food = int(input("원하시는 반찬의 번호를 선택해주세요\n"))
                if food == 0:
                    self.print_intro_menu()
                elif food in self.menu_dict_1:
                    self.menu_dict_1[food]()
                    self.print_return_menu()
                else:
                    self.print_failed_menu()
        except ValueError:
            self.print_error_message()

    def select_menu(self):
        try:
            dinner = int(input(""))
            if dinner == 4:
                print_soup()
                food = int(input("원하시는 국의 번호를 선택해주세요.\n"))
                if food == 0:
                    self.print_intro_menu()
                elif food in self.menu_dict_2:
                    self.menu_dict_2[food]()
                    self.print_return_menu()
                else:
                    self.print_failed_menu()
        except ValueError:
            self.print_error_message()

    # oo식단짜기 기능 구현
    def create_diet(self):
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
            if selected_list is list_a and len(result_a) < 7 and total_sum + selected_number >= 4000:
                result_a.append(selected_number)
                total_sum += selected_number
            elif selected_list is list_b and len(result_b) < 7 and 4000 <= total_sum + selected_number:
                result_b.append(selected_number)
                total_sum += selected_number
        print("랜덤하게 선택된 반찬의 칼로리:", result_a)
        print("랜덤하게 선택된 국의 칼로리:", result_b)
        print("반찬 칼로리의 총합:", sum(result_a))
        print("국 칼로리의 총합:", sum(result_b))
        print("총합:", total_sum)
        print(self.return_menu)


if __name__ == "__main__":
    menu_selector = DinnerLotto()
    menu_selector.print_intro_menu()
    random_menu_one()
    random_menu_two()
    menu_selector.select_side()
    menu_selector.select_menu()
    menu_selector.create_diet()
