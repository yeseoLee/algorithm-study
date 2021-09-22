import sys
input = sys.stdin.readline

#PRIME
max_num=1000001
prime=[True for x in range(max_num)]
prime_nums=[]
for i in range(2,max_num//2 + 1):
    if prime[i]==True:
        for j in range(i+i,max_num,i):
            prime[j]=False
        prime_nums.append(i)


while(True):
    n=int(input())
    if n==0: break
    a,b=-1,-1
    
    for prime_num in prime_nums:
        if prime[n-prime_num]==True:
            a,b=prime_num, n-prime_num
            break   
    if a+b:
        print(f"{n} = {a} + {b}")
    else:
        print("Goldbach's conjecture is wrong.")


