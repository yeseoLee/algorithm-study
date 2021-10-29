'''boolean 배열
import sys
input = sys.stdin.readline

m=int(input())
s = [False]*21
for i in range(m):
    cmd = input().strip().split()
    if len(cmd)==1:
        if cmd[0] == "all" :
            s=[True]*21
        else:
            s=[False]*21

    if cmd[0] == "add":
        if not s[int(cmd[1])]:
            s[int(cmd[1])]=True
    elif cmd[0] == "remove":
        if s[int(cmd[1])]:
            s[int(cmd[1])] = False
    elif cmd[0] == "check":
        if s[int(cmd[1])]:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if s[int(cmd[1])]:
            s[int(cmd[1])] = False
        else:
            s[int(cmd[1])] = True
'''
'''집합
import sys
input = sys.stdin.readline

M = int(input().rstrip())
S = set()

for _ in range(M):
    cal = input().rstrip()
    if cal == 'empty':
        S = set()
    elif cal == 'all':
        S = 
    else:
        cal, num = cal.split()
        if cal == 'add':
            S.add(int(num))
        elif cal == 'remove':
            S.discard(x)
        elif cal == 'check':
            print(1 if int(num) in S else 0)
        else:
            if int(num) in S:
                S.remove(int(num))
            else:
                S.add(int(num))
'''
#비트 연산
import sys
input = sys.stdin.readline

m = int(input())
bit = 0
for i in range(m):
    cmd = input().strip().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            bit= (1 << 21) -1
        else:
            bit = 0
    if cmd[0] == "add":
        bit |= (1 << int(cmd[1]))
    elif cmd[0] == "remove":
        bit &= ~(1 << int(cmd[1]))
    elif cmd[0] == "toggle":
        bit ^= (1 << int(cmd[1]))
    elif cmd[0] == "check":
        if bit & (1 << int(cmd[1])):
            print(1)
        else:
            print(0)
