import sys
import heapq
input = sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
result=[[]]

def dijkstra(start):
    costs=[-1]*(n+1)
    costs[start]=0
    h=[]
    for next in graph[start]: # next-> tuple
        heapq.heappush(h,next)
    while(h):
        cost,now = heapq.heappop(h)
        if costs[now]!=-1 and costs[now]<=cost:
            continue
        costs[now]=cost
        if now<start:
            for i in range(1,n+1):
                if not result[now][i]:
                    continue
                elif costs[i]==-1:
                    costs[i]=cost+result[now][i])
                else:
                    costs[i]=min(costs[i],cost+result[now][i])
            continue
        for next_cost,next_city in graph[now]:
            heapq.heappush(h,(cost+next_cost,next_city))
    costs = list(map(lambda x : 0 if (x<0) else x, costs))
    return costs

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((c,b)) #a:start, b:end, c:cost

for i in range(1,n+1):
    costs = dijkstra(i)
    result.append(costs)
    print(*costs[1:])


'''
n = int(input())
m = int(input())
inf = 100000000
s = [[inf] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    if s[a - 1][b - 1] > c:
        s[a - 1][b - 1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
for i in s:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
'''
