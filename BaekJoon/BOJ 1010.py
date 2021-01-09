import sys
from math import factorial as f 
t=int(sys.stdin.readline())

for i in range(t):
    n,m=map(int,sys.stdin.readline().split())
    mCn=f(m)//(f(m-n)*f(n))
    print(mCn)
