import sys

input = sys.stdin.readline

stack = []

n = int(input())
for i in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        print(int(len(stack) == 0))
    elif cmd[0] == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
