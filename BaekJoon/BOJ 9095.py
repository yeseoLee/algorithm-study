dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,11):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

t=int(input())
for i in range(t):
    n=int(input())
    print(dp[n])




'''
1
(1)

11
2
(2)

111
12
21
3
(4)

1111
112
121
211
22
13
31
(7)

11111
1112
1121
1211
2111
122
212
221
113
131
311
23
32
(13)
'''





