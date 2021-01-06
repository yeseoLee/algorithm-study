import sys
dp=[[[0 for col in range(21)] for row in range(21)] for depth in range(21)]

def w(a,b,c):
    if(a<=0 or b<=0 or c<=0):
        return 1
    elif(a>20 or b>20 or c>20):
        return w(20,20,20)
    elif(dp[a][b][c]):
        return dp[a][b][c]
    elif(a<b<c):
        dp[a][b][c]= w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[a][b][c]= w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

while(True):
    a,b,c=map(int,sys.stdin.readline().split())
    if(a==-1 and b==-1 and c==-1):
        break
    result=f"w({a}, {b}, {c}) = {w(a,b,c)}"
    print(result)

"""
import sys
dp=[[[0 for col in range(21)] for row in range(21)] for depth in range(21)]
for a in range(21):
    for b in range(21):
        for c in range(21):
            if(a==0 or b==0 or c==0):
                dp[a][b][c]=1
            elif(a<b<c):
                dp[a][b][c]=dp[a][b][c-1]+dp[a][b-1][c-1]-dp[a][b-1][c]
            else:
                dp[a][b][c]=dp[a-1][b][c]+dp[a-1][b-1][c]+dp[a-1][b][c-1]-dp[a-1][b-1][c-1]
                
while(True):
    a,b,c=map(int,sys.stdin.readline().split())
    if(a==-1 and b==-1 and c==-1):
        break
    elif(a<0 or b<0 or c<0):
        w=1
    elif(a>20 or b>20 or c>20):
        w=dp[20][20][20]
    else:
        w=dp[a][b][c]
    result=f"w({a}, {b}, {c}) = {w}"
    print(result)
"""
