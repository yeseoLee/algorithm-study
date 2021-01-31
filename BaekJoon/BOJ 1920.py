import sys

def search(li,n):
    L,R=0,len(li)-1
    while(L<=R):
        center=(L+R)//2
        if(li[center]==n):
            return 1
        elif(li[center]>n):
            R=center-1
        else:
            L=center+1
    return 0

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().rstrip().split()))

a=sorted(a)
for i in b:
    print(search(a,i))

"""
import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().rstrip().split()))

for elem in b:
    if (elem in a):
        print(1)
    else:
        print(0)
"""
