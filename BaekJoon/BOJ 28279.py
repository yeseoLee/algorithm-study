import sys
from collections import deque


input = sys.stdin.readline

deck = deque()


def is_empty():
    return len(deck) == 0


n = int(input())
for i in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        deck.appendleft(cmd[1])
    elif cmd[0] == 2:
        deck.append(cmd[1])
    elif cmd[0] == 3:
        if is_empty():
            print(-1)
        else:
            print(deck.popleft())
    elif cmd[0] == 4:
        if is_empty():
            print(-1)
        else:
            print(deck.pop())
    elif cmd[0] == 5:
        print(len(deck))
    elif cmd[0] == 6:
        print(int(is_empty()))
    elif cmd[0] == 7:
        if is_empty():
            print(-1)
        else:
            print(deck[0])
    elif cmd[0] == 8:
        if is_empty():
            print(-1)
        else:
            print(deck[-1])
