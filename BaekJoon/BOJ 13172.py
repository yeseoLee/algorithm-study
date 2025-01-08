import sys

input = sys.stdin.readline


def solution(N, S, X):
    def _gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    # 분할정복을 이용한 거듭제곱
    def _power(a, b):
        ret = 1
        while b:
            if b & 1:
                ret = ret * a % X
            b = b // 2
            a = a * a % X
        return ret

    # 기약 분수 형태로 만들기
    gcd = _gcd(N, S) if N > S else _gcd(S, N)
    a, b = S // gcd, N // gcd

    # b의 모듈러 곱셈의 역원 구하기
    b_i = _power(b, X - 2)

    # a x b^-1 mod(X)
    return (a * b_i) % X


X = 1000000007
result = 0

M = int(input())
for i in range(M):
    N, S = map(int, input().split())
    result += solution(N, S, X)

print(result % X)
