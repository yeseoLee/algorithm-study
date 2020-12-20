import sys
from math import factorial as fac
def nCk(n,k):
    return fac(n)//(fac(k)*fac(n-k))

n,k=map(int,sys.stdin.readline().split())
result=nCk(n,k)%10007
print(result)
