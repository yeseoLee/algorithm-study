# 27172 골드5 수 나누기 게임

import sys
input = sys.stdin.readline

# input
N = int(input())
X = list(map(int,input().split()))

# init
MAX = 1000000

score = [0] * (MAX+1)
exist = [False] * (MAX+1)

# logic
for x in X:
    exist[x] = True

for i in sorted(X):
    for j in range(i*2, MAX+1, i):
        if exist[j]:
            score[i]+=1
            score[j]-=1

# output
for x in X:
    print(score[x],end=" ")   
print()
