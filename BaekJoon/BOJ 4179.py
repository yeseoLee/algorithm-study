import sys
from collections import deque

input = sys.stdin.readline

# 1 <= R,C <= 1000
R, C = map(int, input().split())

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
maze = [list(input().rstrip()) for _ in range(R)]
visited_fire = [[False for i in range(C)] for j in range(R)]

start_fire = []
for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            start_player = (i, j)
        if maze[i][j] == "F":
            start_fire.append((i, j))
            visited_fire[i][j]=True

dx = [0, 0, -1, +1]
dy = [+1, -1, 0, 0]


def can_fire_move(x, y):
    if (0 <= x < R and 0 <= y < C):
        if not visited_fire[x][y]:
            if maze[x][y] == '.' or maze[x][y] == 'J':
                return True
    return False


def fire(fire_que: deque):
    fire_que_next = deque()
    while fire_que:
        x, y = fire_que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if can_fire_move(nx, ny):
                visited_fire[nx][ny] = True
                maze[nx][ny] = "F"
                fire_que_next.append((nx, ny))
    return fire_que_next


def can_player_move(x, y):
    if (0 <= x < R and 0 <= y < C):
        if maze[x][y] == '.':
            return True
    return False


def escape(x, y):
    return (x == 0 or x == R-1 or y == 0 or y == C-1)


def player(player_que: deque):
    player_que_next = deque()
    while player_que:
        x, y = player_que.popleft()
        if escape(x, y):
            return True, deque()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if can_player_move(nx, ny):
                maze[nx][ny] = "J"
                player_que_next.append((nx, ny))
    return False, player_que_next


time = 0
fire_que = deque(start_fire)
player_que = deque([start_player])

while player_que:
    # print("DEBUG:: maze")
    # for m in maze: print(*m)
    # print("DEBUG:: fire")
    # for f in visited_fire: print(f)

    time += 1
    fire_que = fire(fire_que)
    is_escape, player_que = player(player_que)
    if is_escape:
        print(time)
        exit(0)

print("IMPOSSIBLE")
