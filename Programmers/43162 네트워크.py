def solution(n, computers):

    cnt = 0
    visited = [False] * n

    def dfs(k):
        for idx, val in enumerate(computers[k]):
            if val == 1 and not visited[idx]:
                visited[idx] = True
                dfs(idx)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            cnt += 1

    return cnt
