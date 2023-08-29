numbers = [10, 20, 30, 40, 50]
def sum_elements(elements):
    sum = 1
    for elements in numbers:
        sum *= elements
    return sum

print(sum_elements(numbers))