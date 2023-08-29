from dataclasses import dataclass
import csv
@dataclass
class Person:
    name:str
    age:int
    city:str
people = [
Person("홍길동", 30, "뉴욕"),
Person("밥", 25, "갈비"),
Person("샤를라이", 35, "시카고"),
]
with open("사람.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["이름", "나이", "도시"])
    for person in people:
        writer.writerow([person.name, person.age, person.city])
with open("사람.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)