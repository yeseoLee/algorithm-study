from typing import List


# 0 ms / 17.76 MB
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def _dfs(start, tmp):
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                _dfs(i + 1, tmp)
                tmp.pop()
            answer.append(tmp[:])

        _dfs(0, [])
        return answer


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(subset, k):
            for i in range(k, len(nums)):
                dfs(subset + [nums[i]], i + 1)
            result.append(subset)

        dfs([], 0)
        return result
