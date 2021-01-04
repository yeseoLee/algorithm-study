import sys
n=int(sys.stdin.readline())
a=[]
dp=[1 for i in range(n)]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

a= sorted(a, key = lambda x: x[0])
for i in range(n):
    for j in range(i):
        if(a[i][1]>a[j][1]):
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))     
'''
교차
[a b]
[c d]
1. a < c and b > d
2. a > c and b < d

[xn,yn] 에서
1. xn오름차순 and yn오름차순
2. xn내림차순 and yn내림차순

결국 순서가 중요하지 않은 문제이기 때문에
Case1=Case2
'''
