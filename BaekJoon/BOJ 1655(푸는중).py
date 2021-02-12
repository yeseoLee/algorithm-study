from sys import stdin
from queue import PriorityQueue

que=PriorityQueue()
n=int(stdin.readline())

for i in range(1,n+1):
    x=int(stdin.readline())
    que.put(x)
    
        
'''
from sys import stdin
import heapq

heap=[] #최소힙 생성
depth=1 #현재 힙의 깊이
depth_count=1 #현재 깊이의 최대 원소개수
prev_min = 0 #이전 깊이의 원소들 중 최소값
#prev_depth  이전 깊이의 원소들
n=int(stdin.readline())

for i in range(1,n+1):
    x=int(stdin.readline())
    heapq.heappush(heap,x)
    
    if(i==depth_count):
        depth_count+=2**depth
        depth+=1
        prev_depth=heap[depth_count-2**(depth-1):depth_count]
        prev_min=min(prev_depth)
'''

