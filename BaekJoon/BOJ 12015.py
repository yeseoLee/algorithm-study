import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rsplit()))
lis = [] #longest increasing subsequence
ans = 0

for num in a: # O(n)
    if not lis:
        lis.append(num)
        ans += 1
        continue
    
    if lis[-1] < num: # 더 큰 수 -> 수열 뒤에 연결
        lis.append(num)
        ans += 1
    else: #더 작은 수 -> 이진탐색으로 들어갈 위치를 찾아서 기존 값과 교체 O(logn)
        index = bisect_left(lis, num)
        lis[index] = num
    
print(ans)
