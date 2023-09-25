numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num) == even_numbers(numbers)
            return numbers

print(even_numbers(numbers))