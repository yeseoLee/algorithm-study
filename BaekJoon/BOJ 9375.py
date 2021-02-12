from collections import Counter
import sys
 
t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    kind=[]
    for j in range(n):
        a=sys.stdin.readline().split()
        kind.append(a[1])
    count=Counter(kind)
    num=1
    for item in count:
        num*=count[item]+1
    print(num-1)

