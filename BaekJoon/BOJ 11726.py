s = [0, 1, 2]
for i in range(3, 1001):
    s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n] % 10007)
'''
n=int(input())
if(n<=2):
   print(n)
else:
   dp=[0 for _ in range(n+1)]
   dp[1]=1
   dp[2]=2
   for i in range(3,n+1):
       dp[i]=(dp[i-1]+dp[i-2])%10007
   print(dp[n])
'''
