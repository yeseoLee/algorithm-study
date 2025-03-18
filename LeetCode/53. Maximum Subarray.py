from typing import List


# 76ms / 32.63MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = nums[:]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i], dp[i] + dp[i - 1])
        return max(dp)
