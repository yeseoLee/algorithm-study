import sys
def sumFile(ch):
    for i in range(1,k): #길이 
        for j in range(k): #시작점
            if(j+i>=k):
                break
            mincost=99999999
            for x in range(i):
                cost=dp[j][j+x]+dp[j+x+1][j+i]+sum(ch[j:j+i+1])
                if(cost<mincost):
                    mincost=cost
            dp[j][j+i]=mincost

t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    ch=list(map(int,sys.stdin.readline().rstrip().split()))
    dp=[[0]*(k+1) for x in range(k+1)]
    sumFile(ch)
    print(dp[0][k-1])
    
