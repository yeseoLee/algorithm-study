import sys
input=sys.stdin.readline
from collections import deque

def dfs(x,Sum):
    global cnt
    if(x>n-1):
        return
    Sum+=arr[x]
    if(Sum==s):
        cnt+=1
    dfs(x+1,Sum)
    dfs(x+1,Sum-arr[x])

n,s=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
dfs(0,0)
print(cnt)

'''
#1. nC1 + nC2 + nC3 + ...+ nCn-1 + nCn
#2. DFS
'''
