import sys
input=sys.stdin.readline
n,m = map(int,input().split())
dj,bj=set(),set()
for i in range(n):
    dj.add(input().rstrip())
for i in range(m):
    bj.add(input().rstrip())

dbj = sorted(list(dj & bj))
print(len(dbj))
for i in dbj:
    print(i)
