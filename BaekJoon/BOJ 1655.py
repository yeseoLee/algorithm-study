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
    
    if(i=>depth_count):
        depth_count+=2**depth
        depth+=1
    prev_depth=heap[depth_count-2**(depth-1):depth_count]
    prev_min=min(prev_depth)
    print(prev_min)
'''

'''
from sys import stdin
n=int(stdin.readline())

mid=int(stdin.readline())
print(mid)
arr=[mid]
LR=[0]*3
for i in range(n-1):
    x=int(stdin.readline())
    arr.append(x)
    if(mid<x):
        LR[2]+=1
    elif(mid==x):
        LR[1]+=1
    else:
        LR[0]+=1
    if(LR[0]>LR[1]+LR[2]): #중앙값 왼쪽으로 이동
        newmid=-10001
        for i in arr:
            if(newmid<i<mid):
                newmid=i
                LR[1]=0
            elif(newmid==i):
                LR[1]+=1
        mid=newmid #새 중앙값으로 갱신
        LR[2]+=1 #오른쪽 개수 +1
        LR[0]=len(arr)-LR[2]-LR[1]-1
                
    elif(LR[0]+LR[1]+1<LR[2]): #중앙값 오른쪽으로 이동
        newmid=+10001
        for i in arr:
            if(mid<i<newmid):
                newmid=i
                LR[1]=0
            elif(newmid==i):
                LR[1]+=1
        mid=newmid #새 중앙값으로 갱신
        LR[0]+=1 #왼쪽 개수 +1
        LR[2]=len(arr)-LR[1]-LR[0]-1
    print(mid)
'''
