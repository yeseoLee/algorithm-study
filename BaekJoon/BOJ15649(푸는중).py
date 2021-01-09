#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
from math import factorial as f

n,m=map(int,input().split())
#num=f(n)//f(n-m)
num=n**m
f=1
ar = [[] for row in range(num)]
for i in range(m-1):
    num//=n #num//=(n-i)
    f*=n #f*=(n-i)
    for j in range(f):
            for k in range(num):
                ar[num*j+k].append(j%n+1)

for i in range(len(ar)):
    print(ar[i])
