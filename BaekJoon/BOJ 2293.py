'''
import sys
input = sys.stdin.readline

n,k=map(int,input().split())
coin,cnt=[],0
for i in range(n):
    coin.append(int(input()))
coin =sorted(coin)

def dfs(target : int, start : int):
    global cnt
    for i in range(start,n):
        if target-coin[i]==0:
            cnt+=1
            break
        elif target-coin[i]>0:
            dfs(target-coin[i],i)
        else:
            break

dfs(k,0)
print(cnt)
'''
'''
import sys
input = sys.stdin.readline

n,k=map(int,input().split())
coin,cnt=[],0
for i in range(n):
    coin.append(int(input()))
coin =sorted(coin)
dp=[k]

def dfs(c_idx : int):
    global cnt
    for i in range(c_idx,n):
        if dp[-1]-coin[i]==0:
            cnt+=1
            break
        elif dp[-1]-coin[i]>0:
            dp.append(dp[-1]-coin[i])
            dfs(i)
            dp.pop()
        else:
            break

dfs(0)
print(cnt)
'''
from sys import stdin
import sys
input = sys.stdin.readline
n,k=map(int,input().split())
coin,cnt=[],0
for i in range(n):
    coin.append(int(input()))
coin =sorted(coin)
dp=[0]*(k+1)
for c in coin:
    if c > k:
        break
    dp[c]+=1
    for i in range(c+1,k+1):
        dp[i]=dp[i]+dp[i-c]
print(dp[k])


