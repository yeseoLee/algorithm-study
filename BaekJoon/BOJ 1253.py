# BOJ 1253 좋다 https://www.acmicpc.net/problem/1253

# input
n = int(input())
arr = list(map(int, input().split()))

# init
answer = 0

# logic
arr.sort(reverse=True)


def is_good(idx):
    num = arr[idx]
    hubo = set()
    for i in range(n):
        if i == idx:
            continue
        if arr[i] in hubo:
            return True
        hubo.add(num - arr[i])
    return False


for i in range(n):
    if is_good(i):
        answer += 1
# output
print(answer)
