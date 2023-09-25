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