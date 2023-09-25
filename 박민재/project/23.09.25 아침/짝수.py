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

#짝수 for+if
print('1부터 10까지의 짝수를 표시합니다.')
for n in range(1, 11):
    if n%2 == 0:
        print(n)