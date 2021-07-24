import sys
from collections import deque
input=sys.stdin.readline

string=list(input().strip())
m=int(input())

left=deque(string)
right=deque([])
for i in range(m):
    cmd=list(input().strip().split())
    if(cmd[0]=="L"):
        if left:
            right.appendleft(left.pop())
    elif(cmd[0]=="D"):
        if right:
            left.append(right.popleft())
    elif(cmd[0]=="B"):
        if left:
            left.pop()
            #string=string[:cursor-1]+string[cursor:]
    elif(cmd[0]=="P"):
        left.append(cmd[1])
        #string=string[:cursor] + cmd[1] + string[cursor:]
    else:
        print("ERROR")
        
print(''.join(left)+''.join(right))
