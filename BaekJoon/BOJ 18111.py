# BOJ 18111 마인크래프트 

import sys
input = sys.stdin.readline

# input
N, M, B = map(int, input().split())  # B -> count of inventory blocks
BOARD = [list(map(int, input().split()))
         for _ in range(N)]  # N,M -> board size

# init
MIN, MAX = 0, 256
CNT, SUM = N*M, 0

blocks = [0]*(MAX+1)  # idx: height, val: count
for i in range(N):
    for j in range(M):
        blocks[BOARD[i][j]] += 1
        SUM += BOARD[i][j]

result_time = float('inf')
result_height = MAX

# function
def validate_number_of_blocks(target_height: int) -> bool:
    return SUM + B >= target_height * CNT

def calculate_time(target_height: int) -> int:
    time = 0
    for height, count in enumerate(blocks):
        if target_height >= height:  # put -> ls
            time += (target_height-height) * count
        else:  # take -> 2s
            time += (height - target_height) * 2 * count
    return time

# excute
for h in range(MAX, MIN-1, -1):
    if not validate_number_of_blocks(h):
        continue
    t = calculate_time(h)
    if t < result_time:
        result_time = t
        result_height = h

# output
print(result_time, result_height)
