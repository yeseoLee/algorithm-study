#1부터 N까지 자연수 중에서 중복하여 M개를 고른 비 내림차순 수열
n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
visited=[0]*(n+1)
stack=[]
def solve(depth,n,m):
    if(depth==m):
        print(' '.join(map(str,stack)))
        return
    for i in range(1,n+1):
        stack.append(i)
        solve(depth+1,n,m)
        stack.pop()
solve(0,n,m)
'''def product(arr,m):
    for i in range(len(arr)):
        if(m==1):
            yield [arr[i]]
        else:
            for next in product(arr[i:], m-1):
                yield [arr[i]] + next

n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
for i in product(arr,m):
    print(' '.join(map(str,i)))
'''
'''
import itertools
n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
p=list(itertools.product(arr, arr,repeat=m))
#m==2
for i in range(len(arr)):
    print(list(itertools.product([arr[i]], arr[i:])))
#m==3
for i in range(len(arr)):
    print(list(itertools.product([arr[i]], arr[i:],arr[i+1:])))
'''

