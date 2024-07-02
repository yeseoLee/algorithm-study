n = int(input())


def count_squares(n):
    return sum([i**2 for i in range(1, n + 1)])


print(count_squares(n))
