# # BOJ 1039 교환 골드 3

from collections import deque
N, K = map(int, input().split())
M = len(str(N))

def bfs(N, K):
    visited = set()
    visited.add((N, 0))
    q = deque()
    q.append((N, 0))
    answer = 0
    
    while q:
        now, cnt = q.popleft()
        if cnt == K:
            answer = max(answer, now)
            continue
        now = list(str(now))
        for i in range(M-1):
            for j in range(i+1, M):
                if i == 0 and now[j] == '0':
                    continue
                now[i], now[j] = now[j], now[i]
                next = int(''.join(now))
                if (next, cnt+1) not in visited:
                    q.append((next, cnt+1))
                    visited.add((next, cnt+1))
                now[i], now[j] = now[j], now[i]
    return answer if answer else -1

print(bfs(N, K))

'''
전체 케이스를 탐색해야 함 but 내가 제시한 조건은 전체를 커버하지 못함
visited로 중복 케이스만 제거한다면 완전탐색으로 제한시간 내 풀이가 가능한 문제
BFS로 해결했어야 함
'''

# N, K = input().split()
# K = int(K)
# now = list(map(int, N))

# if len(now) == 1 or (len(now) == 2 and now[1] == 0):
#     print(-1)
#     exit(0)

# count = 0
# flag_same_num = False
# for i in range(len(now)):
#     if count == K:
#         break
#     max_idx = i
#     for j in range(i+1, len(now)):
#         if now[j] > now[max_idx]:
#             max_idx = j
#         elif now[j] == now[max_idx]:
#             if max_idx != i:
#                 max_idx = j
#             else:
#                 flag_same_num = True
#     if max_idx == i:
#         continue
#     now[i], now[max_idx] = now[max_idx], now[i]
#     # print("DEBUG::", max_idx, i, now)
#     count += 1

# # print("DEBUG::", now, flag_same_num, K, count)

# if not flag_same_num and (K-count) % 2 == 1:
#     now[len(now)-1], now[len(now)-2] = now[len(now)-2], now[len(now)-1]

# print(''.join(map(str, now)))
