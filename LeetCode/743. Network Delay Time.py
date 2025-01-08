import collections
import heapq
from typing import List


# 373 ms / 19.74 MB
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [-1] * (n + 1)
        distances[k] = 0

        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        h = []
        heapq.heappush(h, (k, 0))
        while h:
            cur_v, cur_d = heapq.heappop(h)
            for nxt_v, nxt_d in graph[cur_v]:
                if distances[nxt_v] == -1 or cur_d + nxt_d < distances[nxt_v]:
                    distances[nxt_v] = cur_d + nxt_d
                    heapq.heappush(h, (nxt_v, cur_d + nxt_d))

        return max(distances[1:]) if -1 not in distances[1:] else -1


class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Graph
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]
        dist = collections.defaultdict(int)

        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))
        if len(dist) == n:
            return max(dist.values())
        return -1
