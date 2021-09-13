import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

ans=0
for i in a:
    if b-i>=0:
        ans+=1
    else:
        ans+= (i-b + c-1)//c + 1

print(ans)
    
