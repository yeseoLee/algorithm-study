import sys
import itertools
from math import factorial as Fac
def score(team):
    s=0
    for i in range(n//2 - 1):
        for j in range(i+1,n//2):
            s+=arr[team[i]][team[j]]+arr[team[j]][team[i]]
    return s

input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))

#능력치 차이의 nC(n//2) 가지 경우의 수
c = Fac(n)//(Fac(n//2))**2
gap=[0]*(c//2)

x=itertools.combinations(range(n),n//2)

for i,idx in zip(x,range(c)):
    #print(i)
    if(idx<c//2):
        gap[idx]+=score(i)
    else:
        gap[c-idx-1]-=score(i)
        gap[c-idx-1]=abs(gap[c-idx-1])

print(min(gap))

'''
123 / 456

12 13
21 23
31 32

(12+21) 
(23 +32)
(13+ 31)

=> 12 13 23

45 46
54 56
64 65

=> 45  46 56

combination

1234 (3*2)

12  34
13  24
14  23

123456 (5*4)

123 456
124 356
125 346
126 345
134 256
135 246
136 245
145 236
146 235
156 234
'''
