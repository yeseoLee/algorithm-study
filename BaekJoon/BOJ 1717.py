'''BFS
import sys
from collections import deque
input = sys.stdin.readline

def bfs(a,b) -> bool : #find b in set_with_a
    visited=[False]*(n+1)
    que=deque([a])
    while(que):
        now=que.pop()
        for new in graph[now]:
            if new == b:
                return True
            if not visited[new]:
                que.append(new)
                visited[new]=True
    return False

n,m=map(int,input().split())
graph=[[] for x in range(n+1)]

for i in range(m):
    x,a,b=map(int,input().split())
    if x==0: #합집합
        graph[a].append(b)
        graph[b].append(a)
    else: #검사
        if bfs(a,b):
            print("YES")
        else:
            print("NO")

'''
'''
import sys
input = sys.stdin.readline
    
n,m=map(int,input().split())
sets = [[x] for x in range(1,n+1)]

for i in range(m):
    x,a,b=map(int,input().split())
    if x==0: #합집합
        for idx,val in enumerate(sets):
            if a in val:
                a_set=idx
            if b in val:
                b_set=idx
        if  a_set != b_set:
            sets[a_set]+=sets[b_set]
            del sets[b_set]

    else: #검사
        for idx,val in enumerate(sets):
            if a in val:
                a_set=idx
            if b in val:
                b_set=idx
        if  a_set==b_set:
            print("YES")
        else:
            print("NO")

'''

import sys
input = sys.stdin.readline
    
n,m=map(int,input().split())
parent = [x for x in range(n+1)]

def find(target):
    if target == parent[target]:
        return target
    else:
        return find(parent[target])

def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b
    

for i in range(m):
    x,a,b=map(int,input().split())
    if x==0: #합집합
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")















            
