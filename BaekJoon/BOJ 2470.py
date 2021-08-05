import sys
input=sys.stdin.readline
n=int(input())
sol=list(map(int,input().split()))

sol.sort()
start,end=0,n-1
neutral_sol=[abs(sol[start]+sol[end]),start,end]

while(start<end):
    x=sol[start]+sol[end]
    if x == 0:
        print(sol[start],sol[end])
        sys.exit(0)
    else:
        if abs(x)<neutral_sol[0]:
            neutral_sol=[abs(x),start,end]
        if x<0: start+=1
        else: end-=1
print(sol[neutral_sol[1]],sol[neutral_sol[2]])
