def nearest_zero(s: str) -> str:
    s = s.split()
    res = []
    rcnt = 0
    lcnt = 0
    for i in range(len(s)):

        for j in s[i:]:
            if '0' not in s[i:]:
                rcnt = len(s) + 2
                break
            if j == '0':
                break
            else:
                rcnt += 1

        for j in s[i:-len(s)-1:-1]:
            if '0' not in s[i:-len(s)-1:-1]:
                lcnt = len(s) + 2
                break
            if j == '0':
                break
            else:
                lcnt += 1

        res.append(str(min(lcnt, rcnt)))
        rcnt = 0
        lcnt = 0

    return ' '.join(res)


# print(nearest_zero('0 1 4 9 0'))
# print(nearest_zero('0 7 9 4 8 20'))
# print(nearest_zero('0 1'))
# print(nearest_zero('1 2 3 0'))
# print(nearest_zero('0 0 0 0 3 3 4 0'))
# print(nearest_zero('0 4 1 0 0'))
