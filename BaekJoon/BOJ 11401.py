'''
1. 파스칼의 삼각형 (dp)
nCk = n-1Ck-1 + n-1Ck
ar=[[0]*(n+1) for _ in range(n+1)]
def pascal(n,k):
    if(ar[n][k]==0):
        if(n==0 or n==k):
            ar[n][k]=1
        elif(k==1 or n-k==1):
            ar[n][k]=n
        else:
            ar[n][k]=pascal(n-1,k-1)+pascal(n-1,k)
    return ar[n][k]
result=pascal(n,k)
print(result%1000000007)
'''

'''
2. 페르마의 소정리 (분할정복)
a^p-1 = 1 (mod p)
(n!%p) * (k!(n-k)!)^(p-2) %p
'''
n,k=map(int,input().split())
p=1000000007
def power(a,b):
    if(b==0):
        return 1
    elif(b%2==0):
        return (power(a,b//2)**2) %p
    else:
        return (power(a,b//2)**2 *a) %p

fac = [1 for _ in range(n+1)]
for i in range(2, n+1):
    fac[i] = fac[i-1] * i % p
fac1 = fac[n]
fac2 = (fac[n-k] * fac[k]) % p

result=(fac1%p) * (power(fac2,p-2)%p)
print(result%p)
