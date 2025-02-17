from typing import List


# 0ms / 17.87MB
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, s, e = 0, 0, len(nums) - 1

        while i <= e:
            if nums[i] == 0:
                nums[i], nums[s] = nums[s], nums[i]
                s += 1
                i = s
            elif nums[i] == 2:
                nums[i], nums[e] = nums[e], nums[i]
                e -= 1
            else:
                i += 1
