n,m=map(int,input().split())
A=[list(map(int,input().split())) for j in range(n)]
m,k=map(int,input().split())
B=[list(map(int,input().split())) for j in range(m)]
C=[[0 for col in range(k)]for row in range(n)]

for i in range(n):
    for j in range(k):
        elem=0
        for e in range(m):
            elem+=A[i][e]*B[e][j]
        C[i][j]=str(elem)

for i in C:
    print(" ".join(i))
