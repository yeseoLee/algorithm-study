# BOJ 2252 줄 세우기 골드3

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(M)]

# case 1. TIME_LIMIT
'''
stack = list()
for v in li:
    flag = False
    prev = list()
    while(len(stack)):
        x = stack.pop()
        prev.append(x)
        if x == v[0]:
            stack.append(v[1])
            while(len(prev)):
                stack.append(prev.pop())
            flag=True
            break
        if x == v[1]:
            stack.append(prev.pop())
            stack.append(v[0])
            while(len(prev)):
                stack.append(prev.pop())
            flag=True
            break
    if not flag:
        stack = prev
        stack.append(v[1])
        stack.append(v[0])
while(len(stack)):
    print(stack.pop(),end= " ")
'''

# case 2. 위상 정렬
graph = [[] for x in range(N+1)]
indegree = [0]*(N+1)
indegree[0] = -1

result = []

for A, B in li:
    graph[A].append(B)
    indegree[B] += 1

que = deque()
for i, v in enumerate(indegree):
    if v == 0:
        que.append(i)

while len(que):
    now = que.pop()
    result.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            que.append(next)
        elif indegree[next] < 0:
            print("CYCLE")
            exit(0)

print(*result)
