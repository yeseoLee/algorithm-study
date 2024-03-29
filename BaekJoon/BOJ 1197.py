import sys
input=sys.stdin.readline
v,e=map(int,input().split())
elist=[]
for i in range(e):
    elist.append(list(map(int,input().split())))
elist.sort(key=lambda x : x[2])
parent=[i for i in range(v+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    if b<a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

result = 0
for s, e,w in elist:
    if find(s) != find(e):
        union(s,e)
        result+=w

print(result)
