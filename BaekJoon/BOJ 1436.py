n = int(input())


def contain_666(x: int) -> int:
    cnt = 0
    while x != 0 and cnt < 3:
        if x % 10 == 6:
            cnt += 1
        else:
            cnt = 0
        x //= 10
    return cnt >= 3


now, answer = 1, 666
while now < n:
    answer += 1
    if contain_666(answer):
        now += 1

print(answer)
