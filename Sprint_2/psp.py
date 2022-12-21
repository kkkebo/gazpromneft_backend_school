d = {}


def psp(n: int) -> set[str] | list[str]:
    if n == 0:
        return {''}

    def gen_parens(k):
        if k not in d:
            d[k] = psp(k)
        return d[k]

    set_of_brackets = set()
    for i in gen_parens(n - 1):
        set_of_brackets.add('(' + i + ')')
        set_of_brackets.add(i + '()')
        set_of_brackets.add('()' + i)

    for j in range(2, n // 2 + 1):
        b = gen_parens(j)
        for i in gen_parens(n - j):
            for k in b:
                set_of_brackets.add(i + k)
                set_of_brackets.add(k + i)

    result = sorted(set_of_brackets)
    return result


n = int(input())
print('\n'.join(psp(n)), end='')
