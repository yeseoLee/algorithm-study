import sys
n=int(sys.stdin.readline())
p=[list(map(int,sys.stdin.readline().strip().split())) for i in range(n)]
cnt=[0,0,0]

def isAllSame(x,y,n):
    k=p[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if(k!=p[i][j]):
                #print(f"{x},{y},{n}X{n},False")
                return False
    #print(f"{x},{y},{n}X{n},True")
    return True

def cut(x,y,n):
    if(n==1):
        cnt[p[x][y]+1]+=1
        return
    else:
        if isAllSame(x,y,n):
            cnt[p[x][y]+1]+=1
            return
        else:
            for i in range(x,x+n,n//3):
                for j in range(y,y+n,n//3):
                    cut(i,j,n//3)

cut(0,0,n)
for i in cnt:
    print(i)

"""
같은 수로 이루어져있는 종이의 개수를 세는 문제
모두 같은 수로 이루어짐-> count+1
else -> 9장으로 나눠서 다시 반복

배열을 쪼개고 만들어서 배열을 함수 인자로 받으려 했으나
비효율적이라 배열은 한번만 선언하고, x,y 좌표를 인자로 받아
좌표만 이동하면서 같은 배열 내에서 지정한 범위(n)내에서 연산을 수행
"""
