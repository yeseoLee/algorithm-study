import sys
from collections import deque
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n,k=map(int,input().split()) #건물 개수 n, 규칙 개수 k
    time=[0]+list(map(int,input().split()))

    dp=[0]*(n+1)
    need=[[] for _ in range(n+1)]
    needed=[[] for _ in range(n+1)]
    
    for i in range(k):
        x,y=map(int,input().split())
        need[y].append(x)
        needed[x].append(y)
    w=int(input())

    #
    print(need)
    print(needed)
    
    que=deque([])
    for i in range(1,n+1):
        if len(need[i])==0:
            que.append(i)

    done=[]
    while(que):
        building=que.popleft()
        done.append(building)

        max_time=0
        for i in need[building]:
            max_time=max(max_time,dp[i])
        dp[building]=time[building]+max_time

        if  building==w:
            break
        
        for i in needed[building]:
            #if set(need[i]).issubset(done):
            if all(elem in done for elem in need[i]):
                que.append(i)
    print(dp[building])
        

        
        

            
            
        
        
    

