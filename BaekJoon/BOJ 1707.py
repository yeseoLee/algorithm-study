import sys
from collections import deque
input=sys.stdin.readline

t=int(input()) #Test Case
for i in range(t):
    v,e=map(int,input().split()) #정점, 간선
    G=[[] for _ in range(v+1)] #그래프 
    label=[-1]*(v+1) #라벨(그룹핑)
    for j in range(e):
        a,b=map(int,input().split()) #그래프에 간선 삽입
        G[a].append(b)
        G[b].append(a)

    que=deque([])
    is_bipartite=True
    for j in range(1,v+1):
        #이분 그래프가 아님
        if not is_bipartite:
            break
        if label[j]==-1:
            que.append(j)
            label[j]=1
            while(que):
                if not is_bipartite:
                    break
                now=que.popleft()
                for next in G[now]:
                    if(label[next]==label[now]): #같은 라벨끼리 이어져 있음
                        is_bipartite=False
                        break
                    elif(label[next]==-1): #방문하지 않은 정점
                        que.append(next)
                        label[next]=(label[now]+1)%2 # 1->0,0->1
                
    if(is_bipartite):
        print("YES")
    else:
        print("NO")
            
        
