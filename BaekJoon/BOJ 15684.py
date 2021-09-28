import sys
#입출력 
input = sys.stdin.readline
n,m,h = map(int,input().split()) # 세로선n, 가로선개수 m, 가능한 가로선 위치 h
dp  = [[0 for col in range(n+2)] for row in range(h+1)]
for i in range(m):
    a,b = map(int,input().split())
    dp[a][b]=1

# ladder game
def move():
    for i in range(1,n+1):
        b=i
        for a in range(1,h+1):
            if dp[a][b]:
                b+=1
            elif dp[a][b-1]:
                b-=1
        if b !=i:
            return 0
    return 1

#BackTraking
def func(idx,c):
    global cnt
    if move() :
        cnt=min(cnt,c)
        return
    if  c == 3:
        return
    for i in range(idx,n):
        for j in range(1,h+1):
            if not dp[j][i-1] + dp[j][i] + dp[j][i+1]:
                dp[j][i] = 1
                func(i,c+1)
                dp[j][i] = 0

cnt=float('inf')
func(1,0)
if cnt==float('inf'):
    print(-1)
else:
    print(cnt)

