import sys
input=sys.stdin.readline

def dice_move(x: int):
    #Top,Bottom,North,South,East,West
    if x==1:
        tmp=side[1]
        side[1]=side[4] #east->bottom
        side[4]=side[0] #top->east
        side[0]=side[5] #west->top
        side[5]=tmp #bottom->west
    elif x==2:
        tmp=side[1]
        side[1]=side[5] #west->bottom
        side[5]=side[0] #top->west
        side[0]=side[4] #east->top
        side[4]=tmp #bottom->east
    elif x==3:
        tmp=side[1]
        side[1]=side[2] #north->bottom
        side[2]=side[0] #top->north
        side[0]=side[3] #south->top
        side[3]=tmp #bottom->south
    else:
        tmp=side[1]
        side[1]=side[3] #south->bottom
        side[3]=side[0] #top->south
        side[0]=side[2] #north->top
        side[2]=tmp #bottom->north

n,m,x,y,k=map(int,input().split())
# n x m board, starting point (x,y), k of command 

board=[]
for i in range(n):
    board.append(list(map(int,input().split())))
cmd=list(map(int,input().split()))

# 0: Top, 1: Bottom, 2: North, 3: South, 4: East, 5: West
side=[x for x in range(6)]
#the numbers on each side of dice
dice_num=[0 for x in range(6)]
for i in cmd:
    if i==1 and y<m-1: #Move East
        y+=1
    elif i==2 and y>0: #Move West
        y-=1
    elif i==3 and x>0: #Move North
        x-=1
    elif i==4 and x<n-1: #Move South
        x+=1
    else:
        continue
    dice_move(i)
    if board[x][y]==0:
        board[x][y]=dice_num[side[1]]
    else:
        dice_num[side[1]]=board[x][y]
        board[x][y]=0
    print(dice_num[side[0]])
