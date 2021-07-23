import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
x=int(input())

nums.sort()

a,b=0,n-1
cnt=0

while(-1<a<b<n):
    #print(nums[a],nums[b])
    if(nums[a]+nums[b]==x):
        cnt+=1
        while(a<b-1 and nums[a]==nums[a+1]):
            a+=1
            cnt+=1
        while(a+1<b and nums[b]==nums[b-1]):
            b-=1
            cnt+=1
        b-=1
        a+=1
    elif(nums[a]+nums[b]>x):
        b-=1
    else:
        a+=1

print(cnt)
        
        
        
