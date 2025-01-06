from typing import List


# 4 ms / 17.82 MB
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []

        def _dfs(start, nums):
            for i in range(start, len(candidates)):
                nums.append(candidates[i])
                if sum(nums) == target:
                    answer.append(nums[:])
                if sum(nums) >= target:
                    nums.pop()
                    return
                else:
                    _dfs(i, nums)
                    nums.pop()

        _dfs(0, [])
        return answer


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(comb, k):
            if sum(comb) == target:
                result.append(comb[:])
                return
            for i in range(k, len(candidates)):
                if sum(comb) + candidates[i] <= target:
                    dfs(comb + [candidates[i]], i)

        dfs([], 0)
        return result
