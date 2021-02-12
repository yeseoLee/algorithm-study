import sys

p=[0]*101
p[1]=1
p[2]=1
p[3]=1
p[4]=2
p[5]=2
t=int(sys.stdin.readline())

for x in range(t):
    n=int(sys.stdin.readline())
    for i in range(6,n+1):
        p[i]=p[i-1]+p[i-5]
    print(p[n])
