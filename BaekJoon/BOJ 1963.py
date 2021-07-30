from collections import deque
import sys
input=sys.stdin.readline

#prime_number
prime=[True]*10000
prime[0],prime[1]=False,False
for i in range(2,len(prime)//2+1):
    if not prime[i]:
        continue
    for j in range(i+i,len(prime),i):
        prime[j]=False

def dfs(now,target):
    if a==b:
        return 0
    flag=-1
    visited=[False]*10000
    que=deque([[now,0]])
    while(que):
        now,cnt=que.popleft()
        if now==target:
            flag=1
            break
        for i in range(4):
            for j in range(0,10):
                if(i==3 and j==0): continue
                next=now + (j-(now%(10**(i+1)))//10**(i))*10**i
                if prime[next] and not visited[next]:
                    visited[next]=True
                    que.append([next,cnt+1])

    if flag: return cnt
    else: return -1

T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    count=dfs(a,b)
    if count==-1:
        print("Impossibile")
    else:
        print(count)
