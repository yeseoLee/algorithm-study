import sys
n=int(sys.stdin.readline())
st=[0 for i in range(301)]
for i in range(n):
    st[i]=int(sys.stdin.readline())

dp=st.copy()
dp[1]+=st[0]
dp[2]+=max(st[0],st[1])
for i in range(3,n):
    dp[i]+=max(dp[i-2],dp[i-3]+st[i-1])

print(dp[n-1])
