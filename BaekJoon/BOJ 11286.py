from sys import stdin
import heapq

heap=[]
n=int(stdin.readline())
for i in range(n):
    x=int(stdin.readline())
    
    if(x!=0):
        heapq.heappush(heap,(abs(x),x))
    elif(len(heap)!=0):
        print(heapq.heappop(heap)[1])
    else:
        print(0)
