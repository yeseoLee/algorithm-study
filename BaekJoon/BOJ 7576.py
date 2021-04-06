from collections import deque
import sys
m,n=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
que=deque([])
newque=deque([])
day=0
# 익은 토마토는 주변 탐색을 위해 큐에 넣는다.
for i in range(n):
    for j in range(m):
        if(arr[i][j]==1):
            que.append([i,j])

#익힘을 전달하는 방향
dx=[+1,-1,0,0]
dy=[0,0,+1,-1]

while(1):
    i,j=que.pop()
    for di,dj in zip(dx,dy):
        #MxN 범위 내에서
        if((i+di)>-1 and (i+di) < n and (j+dj)>-1 and (j+dj) < m):
            #인접한 안익은 토마토를 익힘
            if(arr[i+di][j+dj]==0):
                arr[i+di][j+dj]=1
                #새 큐에 넣음(다음날 사용할 큐)
                newque.append([i+di,j+dj])

    if(len(que)==0):
        if(len(newque)==0):
            break
        else:
            #큐를 전부 비우면 하루 추가하고, 새로 추가한 토마토들로 교체
            que,newque=newque,que
            day+=1
            '''
            for i in range(n):
                for j in range(m):
                    print(arr[i][j],end=" ")
                print()
            print("")
            '''
# 익지 않은 토마토가 있는지
for i in range(n):
    for j in range(m):
        if(arr[i][j]==0):
            print(-1)
            sys.exit()
# 전부익음
print(day)
            

        
