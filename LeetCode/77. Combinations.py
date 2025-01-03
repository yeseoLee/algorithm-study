from typing import List
import itertools


# 131 ms / 59.67 MB
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def _dfs(start, tmp):
            if len(tmp) == k:
                answer.append(tmp[:])
                return
            for i in range(start, n + 1):
                tmp.append(i)
                _dfs(i + 1, tmp)
                tmp.pop()

        _dfs(1, [])
        return answer


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(f):
            if len(prev_elements) == k:
                result.append(prev_elements[:])
            for i in range(f + 1, n + 1):
                prev_elements.append(i)
                dfs(i)
                prev_elements.pop()

        dfs(0)
        return result


class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])
                return
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result


class Solution4:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))
