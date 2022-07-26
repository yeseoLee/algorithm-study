# BOJ 14002
import bisect
import sys

# input
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

lb_indexs = [-1]*n
lb_values = []
max_len = 0
for idx, val in enumerate(arr):
    lower_bound = bisect.bisect_left(lb_values, val)
    lb_indexs[idx] = lower_bound
    if lower_bound == max_len:
        max_len += 1
        lb_values.append(val)
    else:
        lb_values[lower_bound] = val

result = []
now = max_len-1
for i in range(n-1, -1, -1):
    if lb_indexs[i] == now:
        result.append(arr[i])
        now -= 1

print(max_len)
print(*result[::-1])

'''
#BOJ 14002
import sys
# input
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# init
dp = [1]*n
trace = [[] for _ in range(n)]
max_idx = 0

# logic
for i in range(n):
		trace[i].append(arr[i])
    for j in range(i):
        if arr[j]<arr[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
            trace[i] = dp[j][:] + arr[i]
            if dp[i] > dp[max_idx]:
                max_idx = i   
         
# print
print(dp[max_idx])
print(trace[max_idx])
'''
