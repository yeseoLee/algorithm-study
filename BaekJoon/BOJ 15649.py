#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
import itertools

n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
p=list(itertools.permutations(arr,m))
for i in p:
    for j in i:
        print(j,end=" ")
    print()
