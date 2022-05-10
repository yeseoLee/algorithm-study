import sys
from collections import Counter
input = sys.stdin.readline

def find_lr(k,counter):
    can=[]
    for value ,count in counter:
        if count>=k:
            can.append(value)
    if len(can)==0:
        return [-1]

    can.sort()
    max_diff=0
    now_diff=0
    r=can[0]
    for i in range(1,len(can)):
        if can[i] - can[i-1] == 1:
            now_diff+=1
            if max_diff < now_diff:
                max_diff = now_diff
                r = can[i]
        else:
            now_diff = 0
    return [r-max_diff, r]

t=int(input())
for i in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))

    answer = find_lr(k,Counter(a).most_common())

    if len(answer)==1:
        print(answer[0])
    else:
        print(answer[0],answer[1])

# given a,k -> find l,r (r-l is maximized) return l, r or -1 (can't find)
