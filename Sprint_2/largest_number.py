def largest_number(n: int, numbers: str) -> str:
    numbers = numbers.split()
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            res1 = numbers[j] + numbers[j + 1]
            res2 = numbers[j + 1] + numbers[j]
            if res1 < res2:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return ''.join(numbers)


n = int(input())
numbers = input()
print(largest_number(n, numbers))
