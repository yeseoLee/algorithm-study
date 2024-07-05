def solution(n, money):
    answer = 0

    money.sort(reverse=True)

    def pay(n, money):
        if not money:
            return 0

        cnt = 0
        for j in range(n // money[0], -1, -1):
            next_n = n - money[0] * j
            if next_n == 0:
                cnt += 1
            else:
                cnt += pay(next_n, money[1:])
        return cnt % 1000000007

    return pay(n, money)
