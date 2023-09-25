# 사칙연산 클래스
# 변수 2가지 선언 (first, second)

class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.plus = self.plus
        self.multi = self.multi
        self.minus = self.minus
        self.division = self.division

    def plus(self):
        self.plus = self.first + self.second
        print("result :", self.plus)
        return self.plus

    def multi(self):
        self.multi = self.first * self.second
        print("result :", self.multi)
        return self.multi

    def minus(self):
        self.minus = self.first - self.second
        print("result :", self.minus)
        return self.minus

    def division(self):
        self.division = self.first / self.second
        print("result :", self.division)
        return self.division


class Cal(Calculator):
    def division(self):
        if self.second == 0:
            print("result :", self.second)
            return self.second
        else:
            self.division = self.first / self.second
            print("result :", self.division)
            return self.division


#division_cal = Calculator(first=7, second=0)
#division_cal.division()

division_Cal = Cal(7, 0)
division_Cal.division()
