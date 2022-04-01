from collections import deque
import sys
input = sys.stdin.readline

t=int(input())
for i in range(t):
    # keylog: Alphabet, Number, backspace(-), Arrow key()
    keylog = input().rstrip()
    cursor_back=deque()
    cursor_front=[]
    for key in keylog:
        if key=='<':
            if not cursor_front:
                continue
            cursor_back.appendleft(cursor_front.pop())
        elif key=='>':
            if not cursor_back:
                continue
            cursor_front.append(cursor_back.popleft())
        elif key=='-':
            if not cursor_front:
                continue
            cursor_front.pop()
        else:
            cursor_front.append(key)
    print(''.join(cursor_front+list(cursor_back)))
