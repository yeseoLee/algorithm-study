import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        def get_height_bfs(node):
            h = 0
            que = collections.deque([node])
            visited = [False] * n
            visited[node] = True
            while que:
                for i in range(len(que)):
                    now_n = que.popleft()
                    for nxt_n in graph[now_n]:
                        if not visited[nxt_n]:
                            visited[nxt_n] = True
                            que.append(nxt_n)
                h += 1
            return h

        def get_height_dfs(node):
            max_h = 0
            visited = [False] * n
            visited[node] = True
            stack = [(node, 0)]
            while stack:
                now_n, now_h = stack.pop()
                max_h = max(max_h, now_h)
                for nxt_n in graph[now_n]:
                    if not visited[nxt_n]:
                        visited[nxt_n] = True
                        stack.append((nxt_n, now_h + 1))
            return max_h

        heights = [0] * n
        for i in range(n):
            heights[i] = get_height_bfs(i)
        answer = []
        for i, v in enumerate(heights):
            if v == min(heights):
                answer.append(i)
        return answer


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
