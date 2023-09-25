fruits = ["apple", "banana", "banana", "orange", "grape"]
unique_fruits = []
for fruit in fruits:
    if fruits.count(fruit) <= 1:
        unique_fruits.append(fruit)
print(unique_fruits)