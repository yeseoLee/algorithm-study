'''Time limit Exceeded
from collections import deque
x=int(input())

# divide 3, divide 2, minus 1 X => 1

def bfs(x: int) -> int:
    que=deque([[x,[x]]])
    while(que):
        num,arr=que.popleft()
        if num==1:
            return arr
        if num%2==0:
            que.append([num//2,arr+[num//2]])
        if num%3==0:
            que.append([num//3,arr+[num//3]])
        if num>1:
            que.append([num-1,arr+[num-1]])

arr=bfs(x)
print(len(arr)-1)
print(" ".join(map(str,arr)))
'''
# divide 3, divide 2, minus 1 X => 1
x=int(input())
dp=[float('inf')]*(x+1)
trace=[0]*(x+1)
dp[1]=0
for i in range(1,x+1):
    if 3*i<=x and dp[i]+1 < dp[3*i]:
        dp[3*i]=dp[i]+1
        trace[3*i]=i
    if 2*i<=x and dp[i]+1 < dp[2*i]:
        dp[2*i]=dp[i]+1
        trace[2*i]=i    
    if i+1<=x and dp[i]+1 < dp[i+1]:
        dp[i+1]=dp[i]+1
        trace[i+1]=i    

print(dp[x])
print(x,end=" ")
k=trace[x]
while(k>=1):
    print(k,end=" ")
    k=trace[k]



