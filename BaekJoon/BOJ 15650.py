#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열중 오름차순
def permutation(arr,m):
    for i in range(len(arr)):
        if(m==1):
            yield [arr[i]]
        else:
            for next in permutation(arr[i+1:], m-1):
                yield [arr[i]] + next

n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
for i in permutation(arr,m):
    print(' '.join(map(str,i)))

'''
import itertools
n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
p=list(itertools.permutations(arr,m))
p=[list(i) for i in p]
pp=[]
for i in p:
    pp.append(tuple(sorted(i)))
pp=sorted(list(set(pp)))
for i in pp:
    for j in i:
        print(j,end=" ")
    print()
'''
