from math import sqrt

def isprime(n : int):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def get_prime_number_list(n : int):
    prime[0],prime[1]=False,False
    for i in range(2,n//2+1):
        if not prime[i]:
            continue
        for j in range(i+i,n+1,i):
            prime[j]=False

    for idx,val in enumerate(prime):
        if val:
            prime_number.append(idx)

n=13
prime=[True]*(n+1)
prime_number=[]
get_prime_number_list(n)
print(prime_number)
