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
