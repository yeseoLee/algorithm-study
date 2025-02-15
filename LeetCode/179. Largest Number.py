from typing import List


# 39ms / 17.8MB
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"

        nums = [str(num) for num in nums]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                i_num, j_num = nums[i], nums[j]
                i_len, j_len = len(i_num), len(j_num)
                k, flag = 0, False
                while k < 2 * max(i_len, j_len):
                    if i_num[k % i_len] < j_num[k % j_len]:
                        flag = True
                        break
                    elif i_num[k % i_len] > j_num[k % j_len]:
                        break
                    else:
                        k += 1
                if flag:
                    nums[i], nums[j] = nums[j], nums[i]

        return "".join(nums)
