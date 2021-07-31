from collections import deque

def move(ri,rj,bi,bj,d):
    nri,nrj,nbi,nbj=ri,rj,bi,bj
    di,dj=dx[d],dy[d]
    goal=0
    stop=[1,1]
    while(stop[0] or stop[1]):
        if board[nri+di][nrj+dj]=='O':
            goal=1
        if board[nbi+di][nbj+dj]=='O':
            goal=2
            break
        if board[nri+di][nrj+dj]!='#' and (nri+di != nbi or nrj+dj != nbj):
            nri+=di
            nrj+=dj
        else:
            stop[0]=0
        if board[nbi+di][nbj+dj]!='#' and (nbi+di != nri or nbj+dj != nrj):
            nbi+=di
            nbj+=dj
        else:
            stop[1]=0
    return [goal,nri,nrj,nbi,nbj]

def bfs():
    que=deque([])
    que.append(red+blue+[1])
    visit[red[0]][red[1]][blue[0]][blue[1]]=True
    while(que):
        ri,rj,bi,bj,cnt=que.popleft()
        if cnt>10:
            break
        for d in range(4):
            goal,nri,nrj,nbi,nbj=move(ri,rj,bi,bj,d)
            if goal==1:
                return cnt
            elif goal==0:
                if not visit[nri][nrj][nbi][nbj]:
                    visit[nri][nrj][nbi][nbj] = True
                    que.append([nri,nrj,nbi,nbj,cnt+1])
    return -1
                    
n,m=map(int,input().split())
board=[]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]

for i in range(n):
    line=list(input().rstrip())
    for j in range(m):
        if line[j]=='R':
            red=[i,j]
        if line[j]=='B':
            blue=[i,j]
    board.append(line)

dx=[0,0,+1,-1]
dy=[+1,-1,0,0]

print(bfs())                    
            



