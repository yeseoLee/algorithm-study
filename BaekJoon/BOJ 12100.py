import sys
input = sys.stdin.readline # n x n

n=int(input())
board =[ list(map(int,input().split())) for _ in range(n)]

# 4^5 = 2*10 = 1024

def move_up():
    for j in range(n):
        cant=-1 #already combined block
        for i in range(1,n):
            if board[i][j]==0:
                pass
            x,y = i-1,j
            while (x>0 and board[x][y]==0):
                x-=1
            if x!=cant and board[x][y] == board[i][j]:
                board[x][y] += board[i][j]
                board[i][j] = 0
                cant=x
            elif board[x+1][y]==0:
                board[x+1][y] = board[i][j]
                board[i][j] = 0
    for i in board:
        print(i)
            
def move_down():
    for j in range(n):
        cant=n #already combined block
        for i in range(n-1,-1,-1):
            if board[i][j]==0:
                pass
            x,y = i+1,j
            while (x<n and board[x][y]==0):
                x+=1
            if x!=cant and board[x][y] == board[i][j]:
                board[x][y] += board[i][j]
                cant=x
            else:
                board[x-1][y] = board[i][j]
            board[i][j] = 0
    for i in board:
        print(i)

move_up()
