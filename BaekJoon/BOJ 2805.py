def binary(arr,m):
    def wood(x):
        height=0
        for i in arr:
            if(i>x): height+=i-x
        return height
    l,r=0,max(arr)
    while(l<=r):
        mid=(l+r)//2
        if(wood(mid)>=m):
            result=mid
            l=mid+1
        else:
            r=mid-1
    return result

import sys
n,m=map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
print(binary(arr,m))
