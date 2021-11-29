import itertools
import sys
input=sys.stdin.readline

while(True):
    s=list(map(int,input().split()))
    if s[0]==0:
        break
    else:
        lotto=itertools.combinations(s[1:],6)
        for i in lotto:
            print(*i)
        print()
