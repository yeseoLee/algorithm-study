import sys
import heapq
input=sys.stdin.readline
n=int(input())

larger=[]
smaller=[]

median=int(input())
print(median)
for i in range(n-1):
    x=int(input())
    if(x>=median):
        heapq.heappush(larger,x)
    else:
        heapq.heappush(smaller,-x)

    if(len(larger)>len(smaller)+1):
        heapq.heappush(smaller,-median)
        median=heapq.heappop(larger)
    if(len(smaller)>len(larger)):
        heapq.heappush(larger,median)
        median=heapq.heappop(smaller)
        median*=-1
    print(median)

        
    
    
