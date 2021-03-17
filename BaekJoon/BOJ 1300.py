N, K = int(input()), int(input())
start, end = 1, K #(k번째 수는 k를 넘을 수 없다)

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) #mid 이하의 i의 배수 or 최대 N
    
    if temp >= K: #이분탐색 (최소값이므로 같을 때는 줄여아함)
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
