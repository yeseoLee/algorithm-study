n = int(input())
arr = list(enumerate(map(int, input().split()), start=1))
answer = []

now = 0
while len(arr) > 1:
    i, v = arr[now]
    answer.append(i)
    arr.pop(now)

    if v > 0:
        now = (now + (v - 1)) % len(arr)
    else:
        now = (now + v) % len(arr)

# 마지막 남은 요소 추가
answer.append(arr[0][0])
print(*answer)
