def printPermutation(number, digit):
    permutation[digit]=number
    if(digit==n-1):
        for i in permutation:
            print(i,end= ' ')
        print()
        return
    for i in range(1,n+1):
        if(visited[i]): continue
        visited[i]=True
        printPermutation(i,digit+1)
        visited[i]=False

n=int(input())
visited=[False for i in range(n+1)]
permutation=[0]*(n)
for i in range(1,n+1):
    visited[i]=True
    printPermutation(i,0)
    visited[i]=False
