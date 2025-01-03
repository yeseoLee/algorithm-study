from typing import List
import itertools


# 0 ms / 18.16 MB
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = [False] * len(nums)

        def _dfs(tmp):
            if len(tmp) == len(nums):
                answer.append(tmp[:])
                return
            for i, v in enumerate(nums):
                if visited[i]:
                    continue
                visited[i] = True
                tmp.append(v)
                _dfs(tmp)
                tmp.pop()
                visited[i] = False

        _dfs([])
        return answer


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        result = []

        def dfs(permutation):
            for idx, val in enumerate(nums):
                if not visited[idx]:
                    visited[idx] = True
                    dfs(permutation + [val])
                    visited[idx] = False
            if len(permutation) == len(nums):
                result.append(permutation)

        dfs([])
        return result


class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result


class Solution4:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
