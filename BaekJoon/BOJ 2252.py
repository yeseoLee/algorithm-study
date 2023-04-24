# BOJ 2252 줄 세우기 골드3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(M)]

# case 1.
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

# case 2.
front = [[] for x in range(N+1)]
back = [[] for x in range(N+1)]
for A, B in li:
    front[B].append(A)
    back[A].append(B)

result = []
stack = []
for i in range(1, N+1):
    if not back[i] and front[i]:
        result.append(i)
        for v in front[i]:
            result.append(v)
            if i in back[v]:
                back[v].remove(i)
            if v < i and not back[v]:
                stack.append(v)

while len(stack):
    i = stack.pop()
    for v in front[i]:
        result.append(v)
        if i in back[v]:
            back[v].remove(i)
        if not back[v]:
            stack.append(v)

while (len(result)):
    print(result.pop(), end=" ")
