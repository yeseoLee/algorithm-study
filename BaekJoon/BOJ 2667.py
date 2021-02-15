import sys
from collections import deque
def bfs(x,y,cnt):
    if(x>=n or y>=n):
        return
    if(visited[x][y]==False and graph[x][y]==1):
        visited[x][y]==True
        que.append((x,y))
        while(que):
            v=que.popleft()
            graph[v[0]][v[1]]=cnt
            if(visited[v[0]+1][v[1]]==False and graph[v[0]+1][v[1]]==1):
                que.append((v[0]+1,v[1]))
                visited[v[0]+1][v[1]]==True
            if(visited[v[0]-1][v[1]]==False and graph[v[0]-1][v[1]]==1):
                que.append((v[0]-1,v[1]))
                visited[v[0]-1][v[1]]==True
            if(visited[v[0]][v[1]+1]==False and graph[v[0]][v[1]+1]==1):
                que.append((v[0],v[1]+1))
                visited[v[0]][v[1]+1]==True
            if(visited[v[0]][v[1]-1]==False and graph[v[0]][v[1]-1]==1):
                que.append((v[0],v[1]-1))
                visited[v[0]][v[1]-1]==True
        cnt+=1
    bfs(x-1,y,cnt)
    bfs(x+1,y,cnt)
    bfs(x,y-1,cnt)
    bfs(x,y+1,cnt)
        
n=int(sys.stdin.readline())
graph=[]
visited=[[False for i in range(n+2)] f

         ine().rstrip()+'0'))
    graph.append(line)
graph.append([0]*(n+2))

bfs(0,0,2)
print(graph)
