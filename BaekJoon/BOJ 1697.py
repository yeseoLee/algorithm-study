def bfs():
    while(q):
        x,t=q.popleft()
        visited[x]=1
        if(x==k):
            return t
        else:
            if(x-1>=0 and visited[x-1]==0):
                q.append([x-1,t+1])
                visited[x-1]=1
            if(x+1 <=limit and visited[x+1]==0):
                q.append([x+1,t+1])
                visited[x+1]=1
            if(x*2 <=limit and visited[x*2]==0):
                q.append([x*2,t+1])
                visited[x*2]=1

from collections import deque
n,k=map(int,input().split())
limit=100000
visited=[0]*(limit+1)
q=deque([[n,0]])
print(bfs())
