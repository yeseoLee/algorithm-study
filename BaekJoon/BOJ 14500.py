import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

n,m = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

max_sum=0

def dfs(i,j,now_sum,cnt):
    global max_sum
    if i<0 or i>=n or j<0 or j>=m or cnt>4:
        return
    new_sum=now_sum+arr[i][j]
    if cnt==4:
        max_sum=max(max_sum,new_sum)
        return
    dfs(i+1,j,new_sum,cnt+1)
    dfs(i,j+1,new_sum,cnt+1)
    
    if 0<=j-1 and j+1<m: # ㅜ,ㅗ
        dfs(i+1,j,new_sum+arr[i][j-1]+arr[i][j+1],cnt+3)
        dfs(i-1,j,new_sum+arr[i][j-1]+arr[i][j+1],cnt+3)
    if 0<=i-1 and i+1<n: # ㅏ,ㅓ
        dfs(i,j+1,new_sum+arr[i-1][j]+arr[i+1][j],cnt+3)
        dfs(i,j-1,new_sum+arr[i-1][j]+arr[i+1][j],cnt+3)
for i in range(n):
    for j in range(m):
        dfs(i,j,0,1)

print(max_sum)


'''일일이 찾는 방법
n,m=map(int,input().split()) # 세로 N 가로 M
arr=[list(map(int,input().split())) for i in range(n)]
max_sum=[]
for i in range(n):
    for j in range(m):
        tmp=[]
        now_sum=[arr[i][j]]
        now_idx=[[i,j]]
        a,b=i,j
        for _ in range(3):
            if(a>0):
                tmp.append([a-1,b])
            if(a<n-1):
                tmp.append([a+1,b])
            if(b>0):
                tmp.append([a,b-1])
            if(b<m-1):
                tmp.append([a,b+1])
            for old in now_idx:
                if(old in tmp):
                    tmp.remove(old)
            max_num=0
            for A,B in tmp:
                if(max_num<arr[A][B]):
                    max_num=arr[A][B]
                    max_idx=[A,B]
            a,b=max_idx[0],max_idx[1]
            tmp.remove([a,b])
            now_sum.append(arr[a][b])
            now_idx.append([a,b])
        if(sum(now_sum)>sum(max_sum)):
            max_sum=now_sum
print(sum(max_sum))
'''    
'''미리 가능한 모양을 그려놓고 계산
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = []
# 가능한 모든 모양 (19가지)
tetromino = [[[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [3, 0]], 
[[0, 1], [1, 0], [1, 1]], [[1, 0], [2, 0], [2, 1]], 
[[1, 0], [2, 0], [2, -1]], [[0, 1], [0, 2], [1, 0]], 
[[0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [2, 1]], 
[[0, 1], [1, 0], [2, 0]], [[0, 1], [0, 2], [-1, 2]], 
[[1, 0], [1, 1], [1, 2]], [[1, 0], [1, 1], [2, 1]], 
[[1, 0], [1, -1], [2, -1]], [[0, 1], [-1, 1], [-1, 2]], 
[[0, 1], [1, 1], [1, 2]], [[0, 1], [0, 2], [1, 1]], 
[[1, 0], [1, 1], [2, 0]], [[1, 0], [1, -1], [2, 0]], 
[[0, 1], [0, 2], [-1, 1]]]
for i in range(n):
    s.append(list(map(int, input().split())))
result = 0
for i in range(n):
    for j in range(m):
        for k in tetromino:
            try:
                #가능한 조합으로 합을 계산
                sum_n = s[i][j] + s[i + k[0][0]][j + k[0][1]] + s[i + k[1][0]][j + k[1][1]] + s[i + k[2][0]][j + k[2][1]]
            except:
                #N*M 범위를 넘어갈 때
                sum_n = 0
            result = max(result, sum_n)
print(result)
'''

'''DFS로 풀기, ㅏㅓㅗㅜ는 DFS로 풀 수가 없다.
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# ㅗ ㅏ ㅜ ㅓ 모양 
mfinger = [[[0, 1], [0, 2], [-1, 1]], [[0, 1], [0, 2], [1, 1]], 
[[1, 0], [2, 0], [1, 1]], [[1, 0], [1, -1], [2, 0]]]
n, m = map(int, input().split())
s = []
visit = [[0] * m for i in range(n)]
result = 0
def dfs(x, y, cnt, num):
    global result
    if cnt == 4:
        result = max(result, num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, cnt + 1, num + s[nx][ny])
            visit[nx][ny] = 0
def middlefinger(x, y):
    global result
    for i in mfinger:
        try:
            num = s[x][y] + s[x + i[0][0]][y + i[0][1]] + s[x + i[1][0]][y + i[1][1]] + s[x + i[2][0]][y + i[2][1]]
        except:
            num = 0
        result = max(result, num)
for i in range(n):
    s.append(list(map(int, input().split())))
result = 0
for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, s[i][j])
        visit[i][j] = 0
        middlefinger(i, j)
print(result)
'''
