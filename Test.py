n=int(input())
stack=[]
cnt=0
def solve(q,n):
    global cnt
    if(q==0):
        print(stack)
        cnt+=1
        return
    for i in range(n):
        for j in range(n):
            f=0
            for x,y in stack:
                if(i==x or j==y or i-j==x-y):
                    f=1
                    break
            if(f==0):
                stack.append([i,j])
                solve(q-1,n)
                stack.pop()       
solve(n,n)
print(cnt)
