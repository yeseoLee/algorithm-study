import sys
import heapq

input = sys.stdin.readline


def solution(n, m, r, items, graph):
    def _get_item(start):
        q = []
        heapq.heappush(q, (start, 0))
        distance = [m + 1] * (n + 1)
        distance[start] = 0
        while q:
            now, now_d = heapq.heappop(q)
            for nxt, nxt_d in enumerate(graph[now]):
                if nxt_d != 0 and now_d + nxt_d < distance[nxt]:
                    heapq.heappush(q, (nxt, now_d + nxt_d))
                    distance[nxt] = now_d + nxt_d

        li = [i for i, v in enumerate(distance) if v <= m]
        return sum([items[i - 1] for i in li])

    result = 0
    for i in range(1, n + 1):
        result = max(result, _get_item(i))
    return result


n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

print(solution(n, m, r, items, graph))
