def binary(arr,n):
    def count_wire(length):
        count=0
        for i in arr:
            count+=i//length
        return count
    l,r=1,max(arr)
    while(l<=r):
        mid=(l+r)//2
        if(count_wire(mid)>=n):
            result= mid
            l = mid+1
        else:
            r = mid-1
    return result

import sys
k,n=map(int,sys.stdin.readline().split())
arr=[int(sys.stdin.readline().rstrip()) for _ in range(k)]

print(binary(arr,n))
