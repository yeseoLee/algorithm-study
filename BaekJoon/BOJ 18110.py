import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]

if n == 0:
    print(0)
    sys.exit(0)

arr.sort()
trim_n = int(n * 0.15 + 0.5)
arr = arr[trim_n : n - trim_n]
result = int(sum(arr) / len(arr) + 0.5)

print(result)
