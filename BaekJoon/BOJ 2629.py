import sys
input=sys.stdin.readline
cn,chus = int(input()),list(map(int,input().split()))
bn,balls = int(input()),list(map(int,input().split()))

dp=[False]*(sum(chus)+1)
dp[0]=True

for chu in chus:
    for idx, val in enumerate(dp[:]):
        if val:
            dp[idx+chu]=True
for chu in chus:
    for idx,val in enumerate(dp[:]):
        if val and idx-chu>=0:
            dp[idx-chu]=True
    
print(*map(lambda x: 'Y' if x<=sum(chus) and dp[x] else 'N', balls))
