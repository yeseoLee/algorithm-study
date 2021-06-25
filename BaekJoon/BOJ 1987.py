'''
import sys
def dfs(i,j,n):
    max_n[0]=max(n,max_n[0])
    for di,dj in zip([-1,+1,0,0],[0,0,-1,+1]):
        if(i+di>=0 and i+di<r and j+dj>=0 and j+dj<c):
            k=ord(arr[i+di][j+dj])-ord('A')
            if(apb[k]):
                apb[k]=False
                #print(f"{arr[i][j]}->{arr[i+di][j+dj]} : {n+1}")
                dfs(i+di,j+dj,n+1)
                apb[k]=True
            
r,c=map(int,sys.stdin.readline().split()) #r: 세로 c: 가로
arr=[list(sys.stdin.readline().rstrip()) for i in range(r)]
max_n=[0]
apb=[True]*26
apb[ord(arr[0][0])-ord('A')]=False
dfs(0,0,1)
print(max_n[0])
'''

'''
from collections import deque
r,c=map(int,input().split()) #r: 세로 c: 가로
arr=[list(input()) for _ in range(r)]
max_n=0
trace=[arr[0][0]]
que=deque([])
que.append([0,0,trace])
#BFS
while(que):
    i,j,trace=que.pop()
    #print(trace)
    max_n=max(max_n,len(trace))
    for di,dj in zip([-1,+1,0,0],[0,0,-1,+1]):
        if(i+di>=0 and i+di<r and j+dj>=0 and j+dj<c):
            if(arr[i+di][j+dj] not in trace):
                trace.append(arr[i+di][j+dj])
                que.append([i+di,j+dj,trace.copy()])
                trace.pop()
print(max_n)
'''

#set 은 x in arr이 O(1)의 시간을 갖는다.
import sys
r,c=map(int,sys.stdin.readline().split()) #r: 세로 c: 가로
arr=[list(sys.stdin.readline().rstrip()) for _ in range(r)]

dx=[-1,1,0,0]
dy=[0,0,-1,+1]

max_n=1
que=set([(0,0,arr[0][0])])
while(que):
    i,j,trace=que.pop()
    for x in range(4):
        ni,nj=i+dx[x],j+dy[x]
        if(0<=ni<r and 0<=nj<c and arr[ni][nj] not in trace):
            que.add((ni,nj, trace + arr[ni][nj]))
            max_n=max(max_n,len(trace)+1)

print(max_n)
