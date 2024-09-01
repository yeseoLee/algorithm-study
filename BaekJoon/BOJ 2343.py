n, m = map(int, input().split())
arr = list(map(int, input().split()))

# m 개의 칸막이를 세우면 된다
start, end = max(arr), sum(arr)  # 가능한 크기의 최소, 최대로 초기화

while start <= end:
    mid = (start + end) // 2

    sum_v = 0
    cnt = 1
    for v in arr:
        sum_v += v
        if sum_v > mid:
            cnt += 1
            sum_v = v

    if cnt <= m:  # 크기를 mid size로 하면 블루레이 개수가 m개 이하
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
