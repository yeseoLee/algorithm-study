# 골드 3 나머지 합
# https://www.acmicpc.net/problem/10986

n, m = map(int, input().split())
arr = list(map(int, input().split()))

"""
from itertools import accumulate
cumulative_sum = list(accumulate(arr, lambda acc, x: (acc + x) % m))
answer = 0

for i in range(n):
    if cumulative_sum[i] == 0:
        answer += 1
    for j in range(i):
        if cumulative_sum[i] - cumulative_sum[j] == 0:
            answer += 1

print(answer)
"""


r = [0] * m  # m으로 나눈 나머지 담는 곳
prefixSum = 0
for i in range(n):
    prefixSum += arr[i]
    r[prefixSum % m] += 1

ans = r[0]  # 나머지가 0이 되는 경우의 수
for i in range(m):
    # nC2 = n(n-1)/2
    ans += r[i] * (r[i] - 1) // 2
print(ans)
