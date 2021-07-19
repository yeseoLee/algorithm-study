import sys
n=int(input())

if(n==1):
    print(0)
    sys.exit(0)

#get prime number (2~n)
prime=[True]*(n+1)
prime[0],prime[1]=False,False
for i in range(2,n//2+1):
    if prime[i]==True:
        x=i+i
        while(x<=n):
            prime[x]=False
            x+=i
pn=[]
for idx,val in enumerate(prime):
    if val :
        pn.append(idx)

#sum of sequence prime number
start,end=0,0
sum_spn=pn[start]
cnt=0

while(start<=end<len(pn)):
    if(sum_spn==n):
        cnt+=1
        sum_spn-=pn[start]
        start+=1
    elif(sum_spn<n):
        if end==len(pn)-1: break
        end+=1
        sum_spn+=pn[end]
    else:
        sum_spn-=pn[start]
        start+=1

print(cnt)
