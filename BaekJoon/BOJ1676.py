def factorial(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return factorial(n-1)*n
n=int(input())
nfac=str(factorial(n))
cnt=0
for i in range(len(nfac)-1,-1,-1):
    if(nfac[i]!='0'):
        break
    else:
        cnt+=1
print(cnt)
