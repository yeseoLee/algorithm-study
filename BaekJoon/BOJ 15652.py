n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
visited=[0]*(n+1)
stack=[]
def solve(depth,n,m):
    if(depth==m):
        print(' '.join(map(str,stack)))
        return
    if(len(stack)!=0): k=stack[-1]
    else: k=1
    for i in range(k,n+1):
        stack.append(i)
        solve(depth+1,n,m)
        stack.pop()
solve(0,n,m)
'''n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
stack=[]
def solve(depth,arr,m):
    for i in range(len(arr)):
        if(depth==m):
            yield [arr[i]]
        else:
            for next in solve(depth+1,arr[i:],m):
                yield [arr[i]] + next
for x in solve(1,arr,m):
    print(' '.join(map(str,x)))
'''
