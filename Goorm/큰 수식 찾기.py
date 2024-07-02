# https://level.goorm.io/exam/174717/%ED%81%B0-%EC%88%98%EC%8B%9D-%EC%B0%BE%EA%B8%B0/quiz/1

import sys

input = sys.stdin.readline


def operate(x: str) -> int:
    ops = ["+", "-", "*"]
    mul_num = 1
    now_num = 0
    buho = 1
    result = 0

    x = x + "+"  # 마지막 숫자 연산을 위한 연산자 기믹
    for e in x:
        if e not in ops:
            now_num = now_num * 10 + int(e)
        else:
            if e == ops[0]:
                result += buho * mul_num * now_num
                buho, mul_num, now_num = 1, 1, 0
            elif e == ops[1]:
                result += buho * mul_num * now_num
                buho, mul_num, now_num = -1, 1, 0
            else:
                mul_num *= now_num
                now_num = 0

    return result


A, B = input().split()

# print(operate(A),operate(B))
print(max(operate(A), operate(B)))
