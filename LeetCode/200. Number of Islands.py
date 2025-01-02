from typing import List


# 248ms / 20.36MB
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        di, dj = [0, 0, 1, -1], [1, -1, 0, 0]

        def _dfs(i, j):
            grid[i][j] = "-1"
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                        stack.append((ni, nj))
                        grid[ni][nj] = "-1"

        cnt = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    _dfs(i, j)
                    cnt += 1
        return cnt
