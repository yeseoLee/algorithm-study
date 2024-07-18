from collections import deque


def solution(n, wires):
    def get_count(v):
        visited = [0] * (n + 1)
        visited[v] = 1

        # BFS
        que = deque([v])
        while que:
            now = que.popleft()
            for idx, val in enumerate(graph[now]):
                if val == 1 and not visited[idx]:
                    visited[idx] = 1
                    que.append(idx)

        return sum(visited)

    # 그래프 초기화
    graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for v1, v2 in wires:
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    # min_diff 계산
    min_diff = n
    for v1, v2 in wires:
        graph[v1][v2] = 0
        graph[v2][v1] = 0

        v1_cnt = get_count(v1)
        v2_cnt = n - v1_cnt
        diff = abs(v1_cnt - v2_cnt)
        min_diff = min(min_diff, diff)

        graph[v1][v2] = 1
        graph[v2][v1] = 1

    return min_diff
