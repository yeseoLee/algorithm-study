from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


# 33 ms / 19.25 MB
class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        for idx, val in enumerate(sorted(nums)):
            if idx % 2 == 0:
                result += val
        return result
