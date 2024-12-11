from types import List


# 1765 ms / 178.62 MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    answer.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(set(answer))
