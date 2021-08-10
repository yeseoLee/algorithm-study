# 세그먼트 트리 생성
def init(start, end, index):
    if start == end:
        segment_tree[index] = arr[start]
        return segment_tree[index]
    mid = (start + end) // 2
    segment_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return segment_tree[index]

# 세그먼트 트리에서 조건에 맞는 구간 합 구하기
def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

# 배열의 원소가 변경되었을 때 세그먼트 트리도 변경하기
def update(start, end, index, what, value):
    if what < start or what > end:
        return
    segment_tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)

import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

segment_tree = [0] * (N * 4)

init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        b = b - 1
        diff = c - arr[b]
        arr[b] = c
        update(0, N - 1, 1, b, diff)
    elif a == 2:
        print(interval_sum(0, N - 1, 1, b - 1, c - 1))




'''
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split()) #N개의 수, M번의 수 변경, 구간K의 합
num=[int(input()) for _ in range(n)]
change={} #변화량 값
dp=[0]*n #누적합
dp[0]=num[0]
for i in range(1,n):
    dp[i]=dp[i-1]+num[i]
    
for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        change[b-1]=c-num[b-1]
    else:
        #변화 이전 누적합
        result=dp[c-1]-dp[b-1]+num[b-1]
        #변화량 계산
        for key,val in change.items():
            if b-1<=key<=c-1:
                result+=val
        print(result)

'''
            
        
        
