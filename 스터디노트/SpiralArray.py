'''
6 6

  0   1   2   3   4   5
 19  20  21  22  23   6
 18  31  32  33  24   7
 17  30  35  34  25   8
 16  29  28  27  26   9
 15  14  13  12  11  10
위처럼 6 6이라는 입력을 주면 6 X 6 매트릭스에 나선형 회전을 한 값을 출력해야 한다.
'''

def RIGHT(i,j):
    global n,cnt
    if(n==0): return
    for x in range(n):
        matrix[i][j+x]=cnt
        cnt+=1
    n-=1
    DOWN(i+1,j+n)
def DOWN(i,j):
    global m,cnt
    if(m==0): return
    for x in range(m):
        matrix[i+x][j]=cnt
        cnt+=1
    m-=1
    LEFT(i+m,j-1)
def LEFT(i,j):
    global n,cnt
    if(n==0): return
    for x in range(n):
        matrix[i][j-x]=cnt
        cnt+=1
    n-=1
    UP(i-1,j-n)
def UP(i,j):
    global m,cnt
    if(m==0): return
    for x in range(m):
        matrix[i-x][j]=cnt
        cnt+=1
    m-=1
    RIGHT(i-m,j+1)
    
import sys
input=sys.stdin.readline
n,m=map(int,input().split()) #n: 가로,m: 세로
matrix=[[0]*n for _ in range(m)]

# RIGHT -> DOWN -> LEFT -> UP
# n : n~1  // m: m-1 ~ 1
m-=1
cnt=0
RIGHT(0,0)
for x in matrix:
    print(x)

'''
X,Y = map(int,raw_input().split(' '))
lis = [[-1 for i in xrange(Y)] for j in xrange(X)]
x,y = 0,0
dx,dy = 0,1
count = 0
while lis[x][y] == -1:
    lis[x][y] = count
    count+=1
    x,y = x+dx,y+dy
    if x in [-1,X] or y in [-1,Y] or lis[x][y] != -1:
        x,y = x-dx,y-dy
        dx,dy = dy,-dx
        x,y = x+dx,y+dy
for L in lis:
    for val in L:
        print '%3d'%val,
    print
'''
