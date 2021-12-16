'''psudo code
BELLMAN-FORD(G,w,s):
    init-single-source(G,s)
    for i in range(G.V-1): #노드 개수 -1 만큼
        for edge(u,v) in G.E: #모든 엣지에 대해
            RELAX(u,v,w) #가중치 업데이트
    for (u,v) in G.E:
        if v.d > u.d + w(u,v): # is negative cycle
            return False
    return True
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nosun = [list(map(int,input().split())) for _ in range(m)]
inf = 5000001
weight=[inf]*(n+1)
weight[1]=0
'''
for i in range(n-1):
    for s,e,w in nosun:
        if weight[s]==inf:
            continue
        weight[e]=min(weight[e],weight[s]+w)
for s,e,w in nosun:
    if weight[s]!=inf and weight[e] > weight[s]+w:
        print(-1)
        sys.exit()
for i in range(2,n+1):
    if weight[i]!=inf:
        print(weight[i])
    else:
        print(-1)
'''
'''
def bellman_ford():
    #update weight
    for i in range(n):
        for s,e,w in nosun:
            if weight[s]!=inf and weight[e] > weight[s]+w:
                if i==n-1:
                    return False
                weight[e]=weight[s]+w
    return True

if not bellman_ford():
    print(-1)
else:
    for x in weight[2:]:
        print(x) if x!=inf else print(-1)
'''
