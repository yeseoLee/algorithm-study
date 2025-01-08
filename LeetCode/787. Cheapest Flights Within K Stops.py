from typing import List
import collections

import heapq


# 5745 ms / 61.57 MB
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        distances = [[-1 for j in range(k + 1)] for i in range(n)]
        distances[src][0] = 0

        h = [(src, -1, 0)]  # vertex, stops, distance
        while h:
            cur_v, cur_k, cur_d = heapq.heappop(h)
            for nxt_v, nxt_d in graph[cur_v]:
                if (
                    distances[nxt_v][cur_k] == -1
                    or cur_d + nxt_d < distances[nxt_v][cur_k]
                ):
                    distances[nxt_v][cur_k] = cur_d + nxt_d
                    if cur_k + 1 < k:
                        heapq.heappush(h, (nxt_v, cur_k + 1, cur_d + nxt_d))

        if sum(distances[dst]) == -1 * (k + 1):
            return -1

        answer = float("inf")
        for d in distances[dst]:
            if d == -1:
                continue
            answer = min(answer, d)
        return answer


class Solution2:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))  # a->b : cost c
        visit = {}
        q = [(0, src, 0)]  # price,vertex,stops
        while q:
            p, v, s = heapq.heappop(q)
            print(p, v, s)
            if v == dst:
                return p
            if v not in visit or s < visit[v]:
                visit[v] = s
                if s <= k:
                    for nv, np in graph[v]:
                        heapq.heappush(q, (p + np, nv, s + 1))
        return -1


# 왜 방문체크를 안하면 시간초과?
# k번 내에 dst에 방문하지 못하면 k번 Stop 할때까지 다른 노드들이 계속 중복 방문된다. (return -1인 상황)
