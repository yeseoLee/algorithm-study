import sys
from collections import deque
input = sys.stdin.readline

def dslr(a: int,b: int):
    que = deque()
    que.append((a,""))
    while que:
        number,result = que.popleft()
        d = (number * 2) % 10000
        if d == b: return result + "D"
        elif visited[d] == 0:
            visited[d] = 1
            que.append([d, result + "D"])
        s = number - 1 if number != 0 else 9999
        if s == b: return result + "S"
        elif visited[s] == 0:
            visited[s] = 1
            que.append([s, result + "S"])
        l = int(number % 1000 * 10 + number / 1000)
        if l == b: return result + "L"
        elif visited[l] == 0:
            visited[l] = 1
            que.append([l, result + "L"])
        r = int(number % 10 * 1000 + number // 10)
        if r == b: return result + "R"
        elif visited[r] == 0:
            visited[r] = 1
            que.append([r, result + "R"])

        ''' divmod로 처리
        if l_now != 4: t = now*10
        else:
            t, d = divmod(now, 10**(l_now-1))
            t += (d*10)
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'L'))
        if l_now == 1:
            t = now*1000
        else:
            t, d = divmod(now, 10)
            t += (d*1000)
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'R'))
        '''
    return result

t=int(input())
for i in range(t):
    a,b=map(int,input().split()) # 0<=a,b<10000
    visited = [0 for i in range(10000)]
    print(dslr(a,b))
