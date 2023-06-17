# 골드 3 할로윈의 양아치

import sys
from collections import deque
input = sys.stdin.readline

# input 
N,M,K = map(int,input().split()) # 아이들, 친구 관계, 공명 
CANDY = [0] + list(map(int,input().split())) 
FRIENDS = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    FRIENDS[a].append(b)
    FRIENDS[b].append(a)

# friends -> cluster
visited = [False for _ in range(N+1)]
weight = [] 
value = []

def bfs(now: int):
    kids, candy = 1, CANDY[now]
    que = deque([now])
    visited[now] = True

    while que:
        now = que.pop()
        for nxt in FRIENDS[now]:
            if not visited[nxt]:
                kids += 1
                candy += CANDY[nxt]
                visited[nxt] = True
                que.append(nxt)
    return kids , candy

for i in range(1,N+1):
    if not visited[i]:
        kids, candy = bfs(i)
        if kids < K:
            weight.append(kids)
            value.append(candy)

# cluster -> max_candy
# 여기서부터는 배낭 문제인데 이걸 눈치채지 못했음...
len = len(weight)
dp = [[0 for col in range(K+1)] for row in range(len+1)]

for i in range(len+1):
    for w in range(K+1):
        if i==0 or w == 0:
            dp[i][w] = 0
        elif weight[i-1] < w:
            dp[i][w] = max(value[i-1]+dp[i-1][w-weight[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

max_candy = dp[len][K]

'''
max_candy = 0
now_kids = 0
now_candy = 0

def dfs(now: int, now_kids: int, now_candy:int):
    global max_candy
    max_candy = max(max_candy,now_candy)
    for nxt in range(now, len(cluster)):
        kids, candy = cluster[nxt]
        if now_kids+kids < K:
            dfs(nxt+1, now_kids+kids, now_candy+candy)
dfs(0,0,0)
'''

# output
print(max_candy)