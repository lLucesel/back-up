#홀짝분리
numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = []
odd_numbers = []

for num_even in numbers:
    if num_even % 2 == 0:
        even_numbers.append(num_even)

for num_odd in numbers:
    if num_odd % 2 == 1:
        odd_numbers.append(num_odd)

print("짝수:", even_numbers)
print("홀수:", odd_numbers)