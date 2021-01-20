import sys
global blue
blue=0

def s(p):
    result=0
    for i in p:
        result+=sum(i)
    return result
def divide(p,n):
    global blue
    if(s(p)==0):
        return 1
    elif(s(p)==n*n):
        blue+=1
        return 0
    else:
        p1=[[p[i][j] for i in range(n//2)] for j in range(n//2)]
        p2=[[p[i][j] for i in range(n//2,n)] for j in range(n//2)]
        p3=[[p[i][j] for i in range(n//2)] for j in range(n//2,n)]
        p4=[[p[i][j] for i in range(n//2,n)] for j in range(n//2,n)]
        return divide(p1,n//2)+divide(p2,n//2)+divide(p3,n//2)+divide(p4,n//2)

n=int(sys.stdin.readline())
p=[list(map(int,sys.stdin.readline().split())) for i in range(n)]

print(divide(p,n))
print(blue)
