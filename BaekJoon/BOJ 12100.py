import sys
from collections import deque
input = sys.stdin.readline # n x n

#  (O(N^2)) X 4(direction)^5(depth) -> (O(N^2 4^5))
n=int(input())
board =[ list(map(int,input().split())) for _ in range(n)]
ans = 0

def move(k):
    if k ==0:
        move_up()
    elif k==1:
        move_down()
    elif k==2:
        move_left()
    else:
        move_right()
        
def move_up():
    for j in range(n):
        que=deque([])
        x=0
        for i in range(n):
            if board[i][j]!=0:
                que.append(board[i][j])
                board[i][j]=0
        while(que):
            tmp = que.popleft()
            if que and tmp == que[0]:
                tmp+=que.popleft()
            board[x][j]=tmp
            x+=1
            
def move_down():
    for j in range(n):
        que=deque([])
        x=n-1
        for i in range(n):
            if board[i][j]!=0:
                que.append(board[i][j])
                board[i][j]=0
        while(que):
            tmp = que.pop()
            if que and tmp == que[-1]:
                tmp+=que.pop()
            board[x][j]=tmp
            x-=1

def move_left():
    for i in range(n):
        que=deque([])
        x=0
        for j in range(n):
            if board[i][j]!=0:
                que.append(board[i][j])
                board[i][j]=0
        while(que):
            tmp = que.popleft()
            if que and tmp == que[0]:
                tmp+=que.popleft()
            board[i][x]=tmp
            x+=1

def move_right():
    for i in range(n):
        que=deque([])
        x=n-1
        for j in range(n):
            if board[i][j]!=0:
                que.append(board[i][j])
                board[i][j]=0
        while(que):
            tmp = que.pop()
            if que and tmp == que[-1]:
                tmp+=que.pop()
            board[i][x]=tmp
            x-=1

def solve(cnt):
    global board, ans
    if cnt == 5:
        for i in range(n):
            ans = max(ans, max(board[i]))
        return
    b = [x[:] for x in board]
    for k in range(4):
        move(k)
        solve(cnt+1)
        board = [x[:] for x in b]

solve(0)
print(ans)   
