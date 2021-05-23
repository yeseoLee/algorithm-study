'''
n,b=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
result=A.copy()
tmp=[[0]*n for _ in range(n)]
for i in range(b-1):
    for j in range(n):
        for k in range(n):
            for x in range(n):
                tmp[j][k]+=result[j][x]*A[x][k]
            tmp[j][k]%=1000
    result=tmp.copy()
    tmp=[[0]*n for _ in range(n)]

for i in result:
    for j in i:
        print(j,end=" ")
    print()
'''
n,b=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
result=A.copy()
tmp=[[0]*n for _ in range(n)]
for j in range(n):
    for k in range(n):
        for x in range(n):
            tmp[j][k]+=result[j][x]*A[x][k]
        tmp[j][k]%=1000




for i in result:
    for j in i:
        print(j,end=" ")
    print()
