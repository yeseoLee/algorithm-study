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

def matrix(A,b):
    if(b==1):
        for i in range(n):
            for j in range(n):
                A[i][j]%=1000
        return A
    
    elif(b%2==1):
        tmp=[[0]*n for _ in range(n)]
        tmp2=matrix(A,b-1)
        for j in range(n):
            for k in range(n):
                for x in range(n):
                    tmp[j][k]+=tmp2[j][x]*A[x][k]
                tmp[j][k]%=1000
        return tmp
    else:
        tmp=[[0]*n for _ in range(n)]
        tmp2=matrix(A,b//2)
        for j in range(n):
            for k in range(n):
                for x in range(n):
                    tmp[j][k]+=tmp2[j][x]*tmp2[x][k]
                tmp[j][k]%=1000
        return tmp

result=matrix(A,b)
for i in result:
    for j in i:
        print(j,end=" ")
    print()
