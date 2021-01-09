import sys

def sumDigit(n):
    result=n
    for i in str(n):
        result+=int(i)
    """
    ar=list(map(int,str(n)))
    result+=sum(ar)
    """
    return result

n=int(sys.stdin.readline())
a=0

for i in range(n):
    if(sumDigit(i)==n):
        a=i
        break
    
print(a)
