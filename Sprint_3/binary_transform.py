def binary_transform(num: int) -> int:
    if num == 0:
        return 0
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num
    res = ""
    while num != 0:
        res += str(num % 2)
        num = num // 2
    res = int(res[::-1])
    if is_negative:
        return -res
    return res
