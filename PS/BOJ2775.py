"""
a층 b호 
    =(a-1)층 1~b호
    =a층 (b-1)호 + (a-1)층 b호

n층 1호  = 1명
n층 2호 = 1+ (n-1) = n명
n층 3호 = 1+(n-1)+ (n-1)층 3호 
0층 i호는 i명 거주
"""

##재귀코드##
def getNum(a,b):
    if(a==0):
        return b
    elif(b==1):
        return 1
    else:
        return getNum(a,b-1)+getNum(a-1,b)

t=int(input()) #Test Case

for i in range(t):
    k=int(input())
    n=int(input())
    num = getNum(k,n)
    print(num)

##2차원 배열##

ar=[[0]*14 for i in range(15)]
for i in range(14):
    ar[0][i]=i+1 #0층
for i in range(1,15): #1~14층
    for j in range(14):
        if(j==0):
            ar[i][j]=1 #1호
        else:
            ar[i][j]=ar[i-1][j]+ar[i][j-1]

t=int(input()) #Test Case

for i in range(t):
    k=int(input())
    n=int(input())
    print(ar[k][n-1])
