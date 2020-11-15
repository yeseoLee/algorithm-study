"""
k[0] = x[0] * m + d
k[1] = x[1] * m + d
k[2] = x[2] * m + d

k[1]-k[0] = (x[1]-x[0]) * m
k[2]-k[1] = (x[2]-x[1]) * m

두 수k[0]과 k[1]을 m으로 나눴을 때
나머지가 같은 두 수의 차는 m을 약수로 가진다.
가장 큰 m을 찾으면 (최대공약수) 
1을 제외한 m의 약수들이 가능한 숫자들이다.
"""

import sys
import math

n=int(sys.stdin.readline())
a=[int(sys.stdin.readline()) for i in range(n)]
result=[]

for i in range(1,n):
    if(i==1):
        m=(a[1]-a[0])
    else:
        m=math.gcd(a[i]-a[i-1],m)

for i in range(2,int(m**0.5+1)):
    if(m%i==0):
        result.append(i)
        result.append(m//i)

result.append(m)
result = list(set(result))
result.sort()

for i in result:
    print(i,end=" ")
