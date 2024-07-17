def solution(begin, target, words):
    # 변환 가능 여부 확인 함수
    def is_changable(w1: list, w2: list) -> bool:
        cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
        return cnt == 1

    result = []
    visited = [0] * len(words)

    # 탐색 함수
    def dfs(i):
        if words[i] == target:
            result.append(visited[i])
            return
        for nxt in range(len(words)):
            if is_changable(words[i], words[nxt]) and visited[nxt] == 0:
                visited[nxt] = visited[i] + 1
                dfs(nxt)
                visited[nxt] = 0

    # dfs 탐색
    for i in range(len(words)):
        if is_changable(begin, words[i]) and visited[i] == 0:
            visited[i] = 1
            dfs(i)

    # 출력
    if len(result) == 0:
        return 0
    else:
        return min(result)
