import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))

dp=[(k+1) for _ in  range(k+1)]
dp[0]=0

for coin in coins:
    for x in range(coin,k+1):
        dp[x] = min(dp[x],dp[x-coin]+1)

if dp[k]==k+1:
    print(-1)
else:
    print(dp[k])

'''
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))

coins = sorted(coins,reverse=True)

max_size = (k+coins[-1]-1) // coins[-1]
dp=[[] for _ in range(max_size+1)]

dp[0] = coins

for i in range(1,max_size+1):
    for prev in dp[i-1]:
        for coin in coins:
            if prev+coin < k:
                dp[i].append(prev + coin)
            elif prev+coin == k:
                print(i+1)
                sys.exit(0)
    dp[i]=set(dp[i])

print(-1)
'''


'''
가장 비싼 동전 순으로 정렬
12
5
1

k = 30원

12원 2
5원 1
2원 X


12 1
5 0
2 9 (10개)

12 1
5 3
2 X

12 1
5 2
2 4  (7개)

12 1
5 1
2 X

12 X
5 6 
2 0 (6개) 

'''
