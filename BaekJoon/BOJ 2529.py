import sys

input = sys.stdin.readline

k = int(input())
arr = list(input().rstrip().split())
visited = [False] * 10
answer = []


def dfs(tmp):
    i = len(tmp) - 1
    if i == k:
        answer.append(("".join(map(str, tmp))))
        return

    for v in range(10):
        if visited[v]:
            continue
        if (arr[i] == "<" and tmp[-1] < v) or (arr[i] == ">" and tmp[-1] > v):
            visited[v] = True
            tmp.append(v)
            dfs(tmp)
            tmp.pop()
            visited[v] = False


for i in range(10):
    visited[i] = True
    dfs([i])
    visited[i] = False

print(answer[-1])
print(answer[0])
