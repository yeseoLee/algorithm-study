import sys
import heapq
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
cnt=[0]*n
rank=-1
tmp=float('inf')

for i in range(n):
    arr[i]=(arr[i],i)
heapq.heapify(arr)

while(arr):
    x=heapq.heappop(arr)
    if(x[0]!=tmp):
        rank+=1
        tmp=x[0]
    cnt[x[1]]=str(rank)

print(' '.join(cnt))


        
