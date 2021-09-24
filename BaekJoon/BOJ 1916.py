from heapq import heappush,heappop
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
    start,end,cost=map(int,input().split())
    graph[start].append([cost,end])
a,b=map(int,input().split()) #a에서 b까지 가는 비용

inf =float('inf')
cost = [inf for _ in range(n+1)] #각 도시까지 가는 비용
cost[a]=0

q = [(0,a)] # cost값을 기준으로 heap 연산
while q:
    cur_c,cur_n = heappop(q)
    if cost[cur_n] < cur_c: #힙에 추가 된 이후 더 적은 비용이 발견됨
        continue
    for next_c,next_n in graph[cur_n]:
        dist = cur_c + next_c
        if cost[next_n] > dist: #더 적은 비용 -> 갱신 & 큐에 추가
            cost[next_n] = dist
            heappush(q,(dist,next_n))
print(cost[b])
