import sys
from collections import deque
que=deque()
danji=[]

def bfs():
    global danji
    for x in range(1,n+1):
        for y in range(1,n+1):
            if(visited[x][y]==False and graph[x][y]==1):
                visited[x][y]=True
                que.append((x,y))
                cnt=0
                while(que):
                    v=que.popleft()
                    cnt+=1
                    if(visited[v[0]+1][v[1]]==False and graph[v[0]+1][v[1]]==1):
                        que.append((v[0]+1,v[1]))
                        visited[v[0]+1][v[1]]=True
                    if(visited[v[0]-1][v[1]]==False and graph[v[0]-1][v[1]]==1):
                        que.append((v[0]-1,v[1]))
                        visited[v[0]-1][v[1]]=True
                    if(visited[v[0]][v[1]+1]==False and graph[v[0]][v[1]+1]==1):
                        que.append((v[0],v[1]+1))
                        visited[v[0]][v[1]+1]=True
                    if(visited[v[0]][v[1]-1]==False and graph[v[0]][v[1]-1]==1):
                        que.append((v[0],v[1]-1))
                        visited[v[0]][v[1]-1]=True
                danji.append(cnt)
        
n=int(sys.stdin.readline())
graph=[]
visited=[[False for i in range(n+2)] for j in range(n+2)]

graph.append([0]*(n+2))
for i in range(n):
    line=list(map(int,'0'+sys.stdin.readline().rstrip()+'0'))
    graph.append(line)
graph.append([0]*(n+2))

bfs()
danji=sorted(danji)
print(len(danji))
for i in danji:
      print(i)
    
