def solution(key, lock):
    # 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치, 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됨
    def rotate_right(arr):
        n = len(arr)
        ro_arr = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                # (0,0),(0,1),(0,2) -> (0,2),(1,2),(2,2)
                ro_arr[j][n - i - 1] = arr[i][j]
        return ro_arr

    def unlock():
        cnt = 0
        for i in range(m):
            if si + i < 0:
                continue
            if si + i >= n:
                break
            for j in range(m):
                if sj + j < 0:
                    continue
                if sj + j >= n:
                    break
                if lock[si + i][sj + j] == 0 and key[i][j] == 0:
                    return False
                if lock[si + i][sj + j] == 1 and key[i][j] == 1:
                    return False
                if lock[si + i][sj + j] == 0 and key[i][j] == 1:
                    cnt += 1

        return cnt == hole_cnt

    m = len(key)
    n = len(lock)
    hole_cnt = n * n - sum(sum(x) for x in zip(*lock))

    for _ in range(4):
        key = rotate_right(key)
        for si in range(-m + 1, n):
            for sj in range(-m + 1, n):
                if unlock():
                    return True
    return False
