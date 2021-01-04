import sys
n=int(sys.stdin.readline())
s=[]
s=list(map(int,sys.stdin.readline().split()))

l=[0 for i in range(n)]
r=[0 for i in range(n)]
sumlr=[0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if(s[i]>s[j]):
            l[i]=max(l[i],l[j]+1)
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if(s[i]>s[j]):
            r[i]=max(r[i],r[j]+1)
    sumlr[i]=1+l[i]+r[i]

print(max(sumlr))
