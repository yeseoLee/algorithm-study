import sys
input=sys.stdin.readline
n,l=map(int,input().split())

if l%2==0:
    if (n//l * 2 +1)*(l//2) == n:
        return [x for x in range(n//l - l
else:
    if n%l==0:
        return [x for x in range(n//l - l//2, n//l + l//2 +1)]
    else:
        return -1
