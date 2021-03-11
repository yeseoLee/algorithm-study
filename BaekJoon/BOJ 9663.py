def nqueen(n):
    result = []
    dfs(n, 0, [], result)
    return result


def dfs(n, current_row, current_candidate, result):
    # 배치 종료
    if current_row == n:
        result.append(current_candidate[:])
        return

    # current_row에서 배치할 수 있는 col 찾기
    for candidate_col in range(n):
        if possible(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(n, current_row + 1, current_candidate, result)
            current_candidate.pop()


# 이전에 배치한 퀸과 같은 열에 있거나 대각선에 있으면 False
def possible(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

n=int(input())
print(nqueen(n))
