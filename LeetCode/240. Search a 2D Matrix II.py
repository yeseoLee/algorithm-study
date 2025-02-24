import bisect
from typing import List


# 144ms / 23.95 MB
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, answer = 0, False

        while not answer and i < n:
            for j in range(m):
                if matrix[i][j] == target:
                    answer = True
                    break
                elif matrix[i][j] > target:
                    if m == 1:
                        n = i
                    else:
                        m = j
                    break
            i += 1

        return answer


# 136ms / 24.01 MB
class SolutionBisect:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, answer = 0, False

        while not answer and i < n:
            j = bisect.bisect_left(matrix[i], target, lo=0, hi=m)
            if j >= len(matrix[0]):
                pass
            elif matrix[i][j] == target:
                answer = True
            elif matrix[i][j] > target:
                if m == 1:
                    n = i
                else:
                    m = j
            i += 1

        return answer
