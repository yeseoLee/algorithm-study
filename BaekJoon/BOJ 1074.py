import sys
input=sys.stdin.readline

n,r,c=map(int,input().split())
def find(r,c,a,b,k,n):
    if n==1:
        if r==a:
            if c==b:
                print(k)
            else:
                print(k+1)
        else:
            if c==b:
                print(k+2)
            else:
                print(k+3)
        return
    if r<a+2**(n-1):
        if c<b+2**(n-1):
            find(r,c,a,b,k,n-1)
        else:
            find(r,c,a,b+2**(n-1),k+2**(2*n-2),n-1)
    else:
        if c<b+2**(n-1):
            find(r,c,a+2**(n-1),b,k+2**(2*n-2)*2,n-1)
        else:
            find(r,c,a+2**(n-1),b+2**(n-1),k+2**(2*n-2)*3,n-1)
find(r,c,0,0,0,n)
