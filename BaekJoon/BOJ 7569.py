from collections import deque
import sys
m,n,h=map(int,input().split())
arr=[[list(map(int,input().split())) for i in range(n)] for j in range(h)]
que=deque([])
newque=deque([])
day=0

# 익은 토마토는 주변 탐색을 위해 큐에 넣는다.
for i in range(n):
    for j in range(m):
        for k in range(h):
            if(arr[k][i][j]==1):
                que.append([k,i,j])

#익힘을 전달하는 방향
dx=[+1,-1,0,0,0,0]
dy=[0,0,+1,-1,0,0]
dz=[0,0,0,0,+1,-1]

while(1):
    k,i,j=que.pop()
    for di,dj,dk in zip(dx,dy,dz):
        #MxN 범위 내에서
        if((i+di)>-1 and (i+di) < n
        and (j+dj)>-1 and (j+dj) < m
        and (k+dk)>-1 and (k+dk) < h):
            #인접한 안익은 토마토를 익힘
            if(arr[k+dk][i+di][j+dj]==0):
                arr[k+dk][i+di][j+dj]=1
                #새 큐에 넣음(다음날 사용할 큐)
                newque.append([k+dk,i+di,j+dj])

    if(len(que)==0):
        if(len(newque)==0):
            break
        else:
            #큐를 전부 비우면 하루 추가하고, 새로 추가한 토마토들로 교체
            que,newque=newque,que
            day+=1

# 익지 않은 토마토가 있는지
for i in range(n):
    for j in range(m):
        for k in range(h):
            if(arr[k][i][j]==0):
                print(-1)
                sys.exit()
# 전부익음
print(day)

'''꿀팁: 3차원 배열은 [layer][row][colunm] 순이다.'''
        
