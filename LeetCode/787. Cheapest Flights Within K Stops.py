class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=collections.defaultdict(list)
        for a,b,c in flights:
            graph[a].append((b,c)) # a->b : cost c
        visit={}
        q=[(0,src,0)] #price,vertex,stops
        while q:
            p,v,s=heapq.heappop(q)    
            print(p,v,s)
            if v==dst:
                return p
            if v not in visit or s<visit[v]:
                visit[v]=s
                if s<=k:
                    for nv,np in graph[v]:
                        heapq.heappush(q,(p+np,nv,s+1))   
        return -1


#왜 방문체크를 안하면 시간초과?
# k번 내에 dst에 방문하지 못하면 k번 Stop 할때까지 다른 노드들이 계속 중복 방문된다. (return -1인 상황)
