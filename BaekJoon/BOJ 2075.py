import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    li = list(map(int, input().split()))
    arr.extend(li)
    arr.sort(reverse=True)
    arr = arr[:n]

print(arr[-1])


# arr = [0] * n
# for i in range(n):
#     li = list(map(int, input().split()))
#     li.sort(reverse=True)

#     now = n - 1
#     for j in range(i):
#         if arr[now] < li[j]:
#             arr[now] = li[j]
#             now += 1

# print(arr[-1])
