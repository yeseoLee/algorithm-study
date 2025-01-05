import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def solution(N, A, M, B):
    answer = []

    subsets = set(A) & set(B)
    while subsets:
        max_val = max(subsets)
        answer.append(max_val)

        ia = A.index(max_val)
        ib = B.index(max_val)
        A = A[ia + 1 :]
        B = B[ib + 1 :]

        subsets = set(A) & set(B)

    print(len(answer))
    print(*answer)


solution(N, A, M, B)
