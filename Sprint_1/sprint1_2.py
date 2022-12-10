def sleight_of_hand(k: int, field: str) -> int:
    cnt = 0
    for elem in set(field.replace('.', '')):
        if field.count(elem) <= k * 2:
            cnt += 1
    return cnt


k = int(input())
s = ''
for i in range(4):
    s += input()

print(sleight_of_hand(k, s))

# print(sleight_of_hand(3, '12312..22..22..2'))
# print(sleight_of_hand(4, '1111999911119911'))
# print(sleight_of_hand(4, '1111111111111111'))
# print(sleight_of_hand(4, '.' * 16))
# print(sleight_of_hand(2, '123456789'))
