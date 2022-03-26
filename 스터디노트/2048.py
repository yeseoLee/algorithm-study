import keyboard
import random
import time
import sys
#init board
board=[[0 for col in range(4)] for row in range(4)]
keys = ["down","up","left","right","q"]

def init_board():
    return

def print_board():
    for i in range(4):
        print(board[i])

def wait_input_key():
    while True:
        for key in keys:
            if keyboard.is_pressed(key):
                time.sleep(0.1)
                return key

def move_combine(key):
    print(key)

def is_full():
    for row in board:
        for item in row:
            if not item:
                return False
    return True

def get_number():
    return random.choices([2,4],weights=[9,1])[0]

def get_position():
    position = random.randrange(0,16) # 0~15
    pos_x, pos_y = divmod(position,4)
    return (pos_x,pos_y)

def create_number():
    if is_full():
        return False
    number = get_number()
    x,y=get_position()
    while board[x][y]:
        x,y=get_position()
    board[x][y]=number
    return True

if __name__ == "__main__":
    init_board()
    while(True):
        key = wait_input_key()
        if key=="q":
            print("프로그램 종료")
            break
        move_combine(key)
        win_flag = create_number()
        if not win_flag:
            print("게임 오버")
            break
        print_board()
