import sys
input = sys.stdin.readline

'''
def isPalindrome(s,e):
    if s==1 and arr[s-1:e] == arr[e-1::-1]:
        return 1
    elif arr[s-1:e] == arr[e-1:s-2:-1]:
        return 1
    else:
        return 0
'''

'''
for i in arr:
    i를 중점으로하는 부분수열에 대해 펠린드롬인지를 저장 dp[s][e]=1 or 0
'''

n=int(input())
arr=list(map(int,input().split()))
m=int(input())

dp=[[0 for x in range(n)] for y in range(n)]
for i in range(n):
    dp[i][i]=1
    l,r=i-1,i+1
    #홀수
    while(l>=0 and r<=n-1):
        if arr[l] == arr[r]:
            dp[l][r]=1
        else:
            break
        l-=1
        r+=1
    #짝수
    l,r=i,i+1
    while(l>=0 and r<=n-1):
        if arr[l] == arr[r]:
            dp[l][r]=1
        else:
            break
        l-=1
        r+=1
for i in range(m):
    s,e=map(int,input().split())
    print(dp[s-1][e-1])
