'''
바이러스 탐색
모든 바이러스 격리 가능한지
가능하면 가장 넒은 영역을 남기고 출력
불가능하면 벽을 이용해 가장 큰 안전 영역을 만들어 출력
'''

'''
바이러스 큐
빈 공간 리스트

빈공간 리스트에 대하여
    공간 A
        공간 B
            공간 C
                바이러스 큐에 대하여
                    인접한 빈 공간을 BFS로 탐색하며 바이러스 전이
                    안전 지대 개수 COUNT
                MAX( MAX_COUNT , COUNT)
    A,B,C 원 상태로 초기화
    
return MAX_COUNT

'''
from collections import deque
from copy import deepcopy

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
empty = []
infect = deque()
max_cnt = 0

for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            empty.append((i,j))
        elif board[i][j]==2:
            infect.append((i,j))

#벽을 세울 빈공간 3개 선택
for a in range(len(empty)-2):
    board[empty[a][0]][empty[a][1]]=1
    for b in range(a+1, len(empty)-1):
        board[empty[b][0]][empty[b][1]]=1
        for c in range(b+1, len(empty)):
            board[empty[c][0]][empty[c][1]]=1

            #현재 보드&바이러스 복사
            cur_board=deepcopy(board)
            cur_infect=deepcopy(infect)
            # BFS로 보드 탐색하며 바이러스 전이
            while(cur_infect):
                i,j=cur_infect.popleft()
                di,dj = [0,0,+1,-1],[+1,-1,0,0] #상하좌우
                for k in range(4):
                    ni,nj=i+di[k],j+dj[k]
                    if 0 <= ni < n and 0 <= nj < m and cur_board[ni][nj]==0:
                        cur_infect.append((ni,nj))
                        cur_board[ni][nj]=2

            #안전지대 계산
            safe_cnt=0
            for row in cur_board:
                safe_cnt +=row.count(0)
            max_cnt=max(max_cnt,safe_cnt)

            #빈 공간 상태로 복구
            board[empty[c][0]][empty[c][1]]=0
        board[empty[b][0]][empty[b][1]]=0
    board[empty[a][0]][empty[a][1]]=0
            
print(max_cnt)
