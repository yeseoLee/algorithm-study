import sys
input = sys.stdin.readline

m=int(input())
s=[]
for i in range(m):
    cmd = input().strip().split()
    if len(cmd)==1:
        if cmd[0] == "all" :
            s=[str(x) for x in range(1,21)]
        else:
            s=[]

    if cmd[0] == "add":
        s.append(cmd[1])
    elif cmd[0] == "remove":
        if cmd[1] in s:
            s.remove(cmd[1])
    elif cmd[0] == "check":
        if cmd[1] in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if cmd[1] in s:
            s.remove(cmd[1])
        else:
            s.append(cmd[1])
