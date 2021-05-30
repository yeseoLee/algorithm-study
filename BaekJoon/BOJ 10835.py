'''
from collections import deque 

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
max_point=0

que=deque([])
que.append([0,0,0])

while(que):
    now=que.pop()
    #카드 더미 소모
    if(now[0]>=n or now[1]>=n):
        max_point=now[2] if max_point<now[2] else max_point
    else:
        #오른쪽만 버리기 
        if(A[now[0]]>B[now[1]]):
            que.append([now[0],now[1]+1,now[2]+B[now[1]]])
        #왼쪽만 버리기
        que.append([now[0]+1,now[1],now[2]])
        #둘다 버리기
        que.append([now[0]+1,now[1]+1,now[2]])

print(max_point)
'''

'''
from collections import deque 
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
max_point=0
dp=[[0]*(n+1) for _ in range(n+1)]

que=deque([])
que.append([0,0,0])

while(que):
    now=que.pop()
    #카드 더미 소모
    if(now[0]>=n or now[1]>=n):
        max_point=now[2] if now[2]>max_point else max_point
        continue
    #오른쪽만 버리기 
    if(A[now[0]]>B[now[1]]):
        if(dp[now[0]][now[1]+1]<=now[2]+B[now[1]]):
            dp[now[0]][now[1]+1] = now[2]+B[now[1]]
            que.append([now[0],now[1]+1,now[2]+B[now[1]]])
    #왼쪽만 버리기
    if(dp[now[0]+1][now[1]]<=now[2]):
        dp[now[0]+1][now[1]] = now[2]
        que.append([now[0]+1,now[1],now[2]])
    #둘다 버리기
    if(dp[now[0]+1][now[1]+1]<=now[2]):
        dp[now[0]+1][now[1]+1] = now[2]
        que.append([now[0]+1,now[1]+1,now[2]])

print(max_point)
'''
'''
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        #오른쪽 
        if(A[i]>B[j] and dp[i][j]+B[j] >dp[i][j+1]):
            dp[i][j+1]=dp[i][j]+B[j]
        #왼쪽
        if(dp[i][j]>dp[i+1][j]):
            dp[i+1][j]=dp[i][j]
        #둘다
        if(dp[i][j]>dp[i+1][j+1]):
            dp[i+1][j+1]=dp[i][j]

print(max(dp[n-1][n-1],dp[n-1][n]))
'''
'''
#Top Down
n=int(input())
A=[0]+list(map(int,input().split()))
B=[0]+list(map(int,input().split()))
dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if(A[i]>B[j]):
            dp[i][j]=max(dp[i][j-1]+B[j],dp[i-1][j],dp[i-1][j-1])
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])

print(dp[n][n])
'''
#Bottom Up

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if(A[i]>B[j]):
            dp[i][j]=max(dp[i][j+1]+B[j],dp[i+1][j],dp[i+1][j+1])
        else:
            dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])
print(dp[0][0])
