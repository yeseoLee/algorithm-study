def isPos(x):
    dp = [0]*n
n=int(input())
arr=list(map(int,input().split()))

max_len=0
start,end=1,n #수열의 길이
while(start<=end):
    mid=(start+end)//2
    for i in range(mid,n+1):
        if(isPos(i)):
            max_len=mid
            l=mid+1 #길이 확대
            break
    else:
        r=mid-1 #길이 축소


5 20 10 30

1 2 2 3
