def dfs(arr):
    
    
n=int(input())
arr=[[0 for row in range(n)]for col in range(n)]
count=0

for i in range(n):
    for j in range(n):
        arr[i][j]=1
        dfs(arr)
