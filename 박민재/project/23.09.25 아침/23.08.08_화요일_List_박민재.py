#짝수
print('1부터 10까지의 짝수를 표시합니다.')
for n in range(1,11):
    if n == 1:
        continue
    if n == 3:
        continue
    if n == 5:
        continue
    if n == 7:
        continue
    if n == 9:
        continue
    print(n)

#짝수
print("1부터 10까지의 짝수를 표시합니다.")
for n in range(2,12,2):
    print(n)

#짝수
print('1부터 10까지의 짝수를 표시합니다.')
for n in range(1, 11):
    if n%2 == 0:
        print(n)

#구구단
for num1 in range(1,10):
    for num2 in range(1,10):
        num3 = num1 * num2
        print(f"{num3}", end=" ")
    print()

#삼각형
for y in range(1,6):
    for x in range(0,y):
        print("*", end=" ")
    print("")

#역삼각형
for y in range(5,0,-1):
    for x in range(0,y):
        print("*", end=" ")
    print("")

#홀수리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)

#홀수리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers =[]
for num in numbers:
        if num % 2 == 1:
            odd_numbers.append(num)
print(odd_numbers)

