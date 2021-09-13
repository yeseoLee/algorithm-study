'''
def check(i,j,k):
    if k==0: #check_column_numbers
        arr=[False]*9
        for x in board[i]:
            if x!=0: arr[x-1]=True

        #check if '0' is only
        only=0
        for idx,val in enumerate(arr):
            if val==False:
                if only == 0:
                    only=idx+1
                else:
                    only=-1 #0이 2개 이상
                    break
        if 1<=only<=9:
            board[i][j]=only
            return True
        else:
            return check(i,j,1)

    if k==1: #check_row_numbers
        arr=[False]*9
        for x in range(9):
            if board[x][j]!=0:
                arr[board[x][j]-1]=True

        #check if '0' is only
        only=0
        for idx,val in enumerate(arr):
            if val==False:
                if only == 0:
                    only=idx+1
                else:
                    only=-1 #0이 2개 이상
                    break
        if 1<=only<=9:
            board[i][j]=only
            return True
        else:
            return check(i,j,2)
    else: #check_box_numbers
        arr=[False]*9
        box = [i//3,j//3]
        for x in range(3):
            for y in range(3):
                if board[box[0]+x][box[1]+y]!=0:
                    arr[board[box[0]+x][box[1]+y]-1]=True

        #check if '0' is only
        only=0
        for idx,val in enumerate(arr):
            if val==False:
                if only == 0:
                    only=idx+1
                else:
                    only=-1 #0이 2개 이상
                    break
        if 1<=only<=9:
            board[i][j]=only
            return True
        else:
            return False

def get_zero_list() -> list :
    zero_list=[]
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                zero_list.append([i,j])
    return zero_list

def solve(zero_list : list):
    if zero_list==[]:
        return
    new_zero_list=[]
    for i,j in zero_list:
        ck = check(i,j,0)
        if not ck:
            new_zero_list.append([i,j])
    solve(new_zero_list)

solve(get_zero_list())

for i in board:
    print(i)

'''
import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
zero_list = []

def check(y, x, v):
    for i in range(9):
        if board[y][i] == v or board[i][x] == v:
            return False
    for i in range((y//3)*3,(y//3)*3+3):
        for j in range((x//3)*3,(x//3)*3+3):
            if board[i][j] == v:
                return False
    return True

def get_zero_list():
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                zero_list.append([i,j])
    return zero_list

def dfs(cur):
    if cur == len(zero_list): return True
    y,x = zero_list[cur]
    for i in range(1,10):
        if check(y,x,i):
            board[y][x]=i
            if dfs(cur+1): return True
            board[y][x]=0
    return False


get_zero_list()
dfs(0)

for i in board:
    print(*i)