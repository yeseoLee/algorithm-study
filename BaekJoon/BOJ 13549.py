import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

dp=[-1]*100001
len=len(dp)
dp[n]=0

que=deque([n])

while (que):
    now = que.pop()
    if now==k:
        break
    for next in (now*2,now-1,now+1):
        if 0<=next<len and dp[next]==-1:
            if next==now*2:
                dp[next] = dp[now]
                que.append(next)
            else:            
                dp[next]=dp[now]+1
                que.appendleft(next)

print(dp[k])


'''
import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())

dp=[-1]*100001
dp[n]=0

que=[]
heapq.heappush(que,[0,n])

while (que):
    time,now = heapq.heappop(que)
    if now==k:
        print(dp[k])
        break
    if now*2<len(dp) and dp[now*2]==-1 :
        dp[now*2] = time
        heapq.heappush(que,[time,now*2])
    if now+1<len(dp) and dp[now+1]==-1 :
        dp[now+1] = time+1
        heapq.heappush(que,[time+1,now+1])
    if now-1>=0 and dp[now-1]==-1 :
        dp[now-1] = time+1
        heapq.heappush(que,[time+1,now-1])
'''
