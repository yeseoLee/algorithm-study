from sys import stdin
import heapq
n=int(stdin.readline())
maxHeap=[]
for i in range(n):
    x=int(stdin.readline())
    if(x!=0):
        heapq.heappush(maxHeap,(-x,x))
    elif(len(maxHeap)!=0):
            print(heapq.heappop(maxHeap)[1])
    else:
        print(0)
