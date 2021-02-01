"""
def BinaryLeft(arr,t,l,r):
    if(l>r): return 0
    m=(l+r)//2
    if (arr[m]>t):
        return BinaryLeft(arr,t,l,m-1)
    if (arr[m]==t):
        if(m==0 or arr[m-1]!=t): return m
        return BinaryLeft(arr,t,l,m)
    if (arr[m]<t):
        return BinaryLeft(arr,t,m+1,r)
    
def BinaryRight(arr,t,l,r):
    if(l>r): return 0
    m=(l+r)//2
    if (arr[m]>t):
        return BinaryRight(arr,t,l,m-1)
    if (arr[m]==t):
        if(m==len(arr)-1 or arr[m+1]!=t): return m+1
        return BinaryRight(arr,t,m+1,r)
    if (arr[m]<t):
        return BinaryRight(arr,t,m+1,r)

import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().rstrip().split()))
a=sorted(a)
for i in b:
    print(BinaryRight(a,i,0,n-1)-BinaryLeft(a,i,0,n-1))
"""
"""
def BinarySearch(arr,t,l,r):
    if(l>r): return 0
    m=(l+r)//2
    if (arr[m]>t):
        return BinarySearch(arr,t,l,m-1)
    if (arr[m]==t):
        return 1+BinarySearch(arr,t,m+1,r)+BinarySearch(arr,t,l,m-1)
    if (arr[m]<t):
        return BinarySearch(arr,t,m+1,r)

import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().rstrip().split()))
a=sorted(a)
for i in b:
    print(BinarySearch(a,i,0,n-1))
"""
