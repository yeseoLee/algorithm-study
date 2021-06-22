n=int(input())
t=[]
p=[]
for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

profit=[0]*(n+1)
for i in range(n):
    if(t[i]+i<=n):
        profit[i+t[i]]=max(profit[i+t[i]],max(profit[:i+1])+p[i])
print(max(profit))
