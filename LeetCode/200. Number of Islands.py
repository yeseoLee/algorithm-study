class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(vi,vj):
            for i in range(4):
                ni,nj = vi+di[i], vj+dj[i]
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]=='1':
                    grid[ni][nj]='0'
                    dfs(ni,nj)
        
        di,dj = [0,0,+1,-1], [+1,-1,0,0]
        m,n=len(grid), len(grid[0])
        result=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    result+=1       
        return result
