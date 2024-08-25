# 실버 2 https://www.acmicpc.net/problem/11722

n = int(input())
arr = list(map(int, input().split()))

answer = [1] * n
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            answer[i] = max(answer[i], answer[j] + 1)

print(max(answer))


# def solution(now, idx):
#     if idx >= n:
#         return 0
#     if now > arr[idx]:
#         return max(1 + solution(arr[idx], idx + 1), solution(now, idx + 1))
#     else:
#         return max(solution(arr[idx], idx + 1), solution(now, idx + 1))


# print(1 + solution(arr[0], 1))
