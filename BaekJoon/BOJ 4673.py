def d(n):
    result=n
    while(n):
        result+=n%10
        n//=10
    return result
ar=[True]*10001

for i in range(1,10001):
    if(d(i)<=10000):
        ar[d(i)]=False

for i in range(1,10001):
    if (ar[i]):
        print(i)
    
    
