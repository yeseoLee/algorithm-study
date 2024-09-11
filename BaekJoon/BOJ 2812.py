from collections import deque

N, K = map(int, input().split())
num_list = list(input().rstrip())

que = deque()

cnt = K
for i, v in enumerate(num_list):
    while que and que[-1] < num_list[i] and cnt > 0:
        que.pop()
        cnt -= 1
    que.append(num_list[i])

que = list(que)[: N - K]
print(int("".join(map(str, que))))
