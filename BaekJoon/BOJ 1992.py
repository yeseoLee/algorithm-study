import sys
def s(p):
    result=0
    for i in p:
        result+=sum(i)
    return result
def QuadTree(p,n):
    if(s(p)==0):
        print('0',end="")
        return
    elif(s(p)==n*n):
        print('1',end="")
        return
    else:
        print('(',end="")
        QuadTree([[p[i][j] for j in range(n//2)] for i in range(n//2)],n//2)
        QuadTree([[p[i][j] for j in range(n//2,n)] for i in range(n//2)],n//2)
        QuadTree([[p[i][j] for j in range(n//2)] for i in range(n//2,n)],n//2)
        QuadTree([[p[i][j] for j in range(n//2,n)] for i in range(n//2,n)],n//2)
        print(')',end="")
        return 

n=int(sys.stdin.readline())
dot=[list(map(int,sys.stdin.readline().strip())) for i in range(n)]
QuadTree(dot,n)
