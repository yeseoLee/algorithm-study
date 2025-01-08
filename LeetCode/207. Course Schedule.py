from typing import List


# 1049 ms / 19.39 MB
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        def _dfs(cur, root):
            for nxt in graph[cur]:
                if nxt == root:
                    return False
                if visited[nxt]:
                    continue
                visited[nxt] = True
                if not _dfs(nxt, root):
                    return False
            return True

        for i in range(numCourses):
            visited = [False] * numCourses
            if not _dfs(i, i):
                return False
        return True


# 7ms / 19.74MB
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)
            return True

        for x in range(numCourses):
            if not dfs(x):
                return False
        return True
