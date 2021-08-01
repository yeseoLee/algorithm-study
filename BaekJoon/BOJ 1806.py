import sys
input=sys.stdin.readline

n,s=map(int,input().split())
nums=list(map(int,input().split()))

start,end=0,0
sub_sum=nums[start]
sub_len=1
min_len=100001

while(start<=end<n):
    if sub_sum>=s:
        min_len=min(min_len,sub_len)
        sub_sum-=nums[start]
        start+=1
        sub_len-=1
    else:
        if end==n-1: break
        end+=1
        sub_sum+=nums[end]
        sub_len+=1

if(min_len==100001):
    print(0)
else:
    print(min_len)
