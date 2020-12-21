import sys

n=int(sys.stdin.readline()) #집의 수
price=[]*n
s=0
for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    price.append(line)
    
"""
조건
1번 != 2번
N번 != N-1번
i번 != i-1번 and i번 != i+1번
-->옆집이랑 겹치면 안된다.
"""

