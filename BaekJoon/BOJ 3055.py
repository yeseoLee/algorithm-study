import sys
from collections import deque

#'S': gosm, 'D': beaver, '*': water , 'X': stone, '.': empty
# INPUT1 = ['D.*','...','.S.']
# INPUT2 = ['D.*','...','..S']
# INPUT3 = ['D...*.','.X.X..','....S.']
# INPUT4 = ['5 4','.D.*','....','..X.','S.*.','....']
#board = list(map(lambda x: list(''.join(x)), INPUT1))
#r,c = len(board),len(board[0])

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(''.join(input().rstrip())) for _ in range(r)]

water_que = deque()
que=deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            water_que.append((i,j))
        elif board[i][j] == 'S':
            que.append((i,j))    

dx,dy = [+1,-1,0,0],[0,0,+1,-1]
time = 0
while(que):
    time+=1
    # water spread
    for _ in range(len(water_que)):
        wx,wy = water_que.popleft()
        for i in range(4):
            nwx,nwy = wx+dx[i],wy+dy[i]
            if 0<=nwx<r and 0<=nwy<c and board[nwx][nwy]=='.':
                board[nwx][nwy]='*'
                water_que.append((nwx,nwy))
    # move gosm
    for _ in range(len(que)):
        x,y = que.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c: 
                if board[nx][ny]=='.':
                    board[nx][ny]='S'
                    que.append((nx,ny))
                elif board[nx][ny]=='D':
                    print(time)
                    sys.exit(0)
    #for i in board:
    #    print(i)    

print("KAKTUS")