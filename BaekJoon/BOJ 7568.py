import sys
input = sys.stdin.readline

n=int(input())
dc=[] # dungchi
rank=[1]*n
for i in range(n):
    x,y=map(int,input().split())
    dc.append((x,y))

for i in range(n):
    for j in range(i+1,n):
        if dc[i][0] > dc[j][0] and dc[i][1] > dc[j][1]:
            rank[j]+=1
        elif dc[i][0] < dc[j][0] and dc[i][1] < dc[j][1]:
            rank[i]+=1
print(*rank)