empty_tuple = ()
tuple_type_1 = (100, 200, 300, 400, 'kiwi', 'cherry')
tuple_type_2 = (1, 2, 3, 4, 'apple', 'banana')

print('빈 튜플 : ',empty_tuple)
print(tuple_type_2[0])
print(tuple_type_2[2])
print(tuple_type_2[3])
print(tuple_type_2[4])

length_tuple_type_2 = len(tuple_type_2)
print(length_tuple_type_2)

#의미없음
synthesis = zip(tuple_type_2, tuple_type_1)
print(synthesis)

synthesis_list = list(synthesis)
print(synthesis_list)




fruits_tuple = ('apple', 'banana', 'orange', 'grape', 'melon')

#인덱스 0부터 3까지
print(fruits_tuple[0:3])
#거꾸로
print(fruits_tuple[::-1])
#인덱스 2부터 끝까지
print(fruits_tuple[2:])
#인덱스 1부터 1씩 건너 뛰이서
print(fruits_tuple[1::1])

fruit1, fruit2, fruit3, fruit4, fruit5 = fruits_tuple
print('첫번째 과일 : ', fruit1)
print('두번째 과일 : ', fruit2)
print('세번째 과일 : ', fruit3)
print('네번째 과일 : ', fruit4)
print('다섯번째 과일 : ', fruit5)
#튜플의 요소과 무한히 늘어날 경우 언팩킹은 어떻게 해야하나?

print(fruits_tuple.index('orange'))
print(fruits_tuple.count('banana'))

#dic
dic_type_1 = {"apple": 1.5, "banana": 2}
dic_type_2 = {
    "fruit": {
        "apple": {
            "price": 100,
            "quantity": 50
        },
        "banana": {
            "price": 70,
            "quantity": 65
        }
    },
    "manager": {
        "John": {
            "age": 30,
            "sub": "Leader"
        },
        "Phode": {
            "age": 28,
            "sub": "buha"
        }
    }
}

dic_type_3 = dict(
    fruit=dict(
        apple=dict(
            price=100, quantities=50
        ),
        banana=dict(
            pricec=70, quantities=65
        )
    )
)

_fruit = dic_type_2['fruit']
print(_fruit)

_fruit_with_get = dic_type_2.get("fruit")
_manager_with_get = dic_type_2.get("manager")

print(_fruit_with_get)
print(_manager_with_get)

_fruit_with_get = dic_type_2.get("fruit____", "키가 없습니다.")
print(_fruit_with_get)
#컨트롤 두번 누른 상태에서 커서를 아래로 하면 여러개 치기 가능
#Ctrl+w 익스텐드 셀렉션 : 커서에 해당하는 단어 선택
print("1223")
print("1223")
print("1223")
print("1223")



dic_type_2["fruit"]["apple"] = {
        "price": 100,
        "quantity": 50,
        "grade": 3
    }
print(dic_type_2)

_pop_item = dic_type_2.pop("fruit")
print(f"dic_type_2 -- {dic_type_2}")
print(f"_pop_item -- {_pop_item}")


empty_set = {}

set_type_1 = {10, 20}
set_type_2 = {"hello", "Python"}

#set_type_1_1 = set([10, 20])
#set_type_1_2 = set(["hello", "Python"])

set_fruit = {"apple", "banana", "mango", "cherry"}
print(f"set_fruit before add -- {set_fruit}")
set_fruit.add("melon")
print(f"set_fruit after add -- {set_fruit}")

set_fruit.update(["strawberry", "blurberry"])
print(f"set_fruit after update -- {set_fruit}")

set_fruit.remove("apple")
#목록에 없는 요소 삭제시 에러
set_fruit.discard("appleeasdfg")
#목록에 없는 요소 삭제시 에러 없음
print(set_fruit)

set_fruit_type_2 = {"apple", "apple", "apple"}
print(set_fruit_type_2)#set은 중복 혀용을 안하기 때문에 apple 하나만 출력
