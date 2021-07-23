import sys
input=sys.stdin.readline
n,m=map(int,input().split())
nums=list(map(int,input().split()))

start,end=0,1
count=0
sum=nums[start]
if sum==m:
    count+=1

while not start==end==n :
    if sum < m and end < n: 
        sum+=nums[end]
        end+=1
    else:
        sum-=nums[start]
        start+=1
    if sum==m:
        count+=1

print(count)        
