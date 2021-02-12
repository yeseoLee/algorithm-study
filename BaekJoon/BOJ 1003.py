import sys

fib = [[0 for col in range(2)] for row in range(41)]
#fib = [[0]*2 for i in range(41)]
fib[0][0]=1
fib[1][1]=1
p=1

t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    if(p<n):
        for i in range(p+1,n+1):
            fib[i][0]=fib[i-1][0]+fib[i-2][0]
            fib[i][1]=fib[i-1][1]+fib[i-2][1]
        p=n
    print(fib[n][0],fib[n][1])
