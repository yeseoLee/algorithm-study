from sys import stdin
import heapq

heap=[]
n=int(stdin.readline())
for i in range(n):
    x=int(stdin.readline())
    if(x!=0):
        heapq.heappush(heap,x)
    elif(len(heap)!=0):
        print(heapq.heappop(heap))
    else:
        print(0)
