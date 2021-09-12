import sys
from collections import deque
input = sys.stdin.readline # n x n

n=int(input())
board =[ list(map(int,input().split())) for _ in range(n)]

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
            
    for i in board:
        print(i)
            
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
            
    for i in board:
        print(i)

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
            
    for i in board:
        print(i)

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
            
    for i in board:
        print(i)


