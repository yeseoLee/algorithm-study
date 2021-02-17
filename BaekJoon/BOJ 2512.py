from sys import stdin

n=int(stdin.readline())
arr=list(map(int,stdin.readline().split()))
limit=int(stdin.readline())
arr=sorted(arr)

l,r=0,arr[-1]
now_max=0
while(l<=r):
    mid=(l+r)//2
    money=0
    for i in arr:
        if(mid>i):
            money+=i
        else:
            money+=mid
    if(money<=limit):
        now_max=mid
        l=mid+1
    else:
        r=mid-1
        
print(now_max)
