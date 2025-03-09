from collections import Counter, defaultdict
from typing import List


# 0ms / 19.46MB
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common()[0][0]


# 3ms / 19.47MB
class SolutionGreedy:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        max_cnt, cur_cnt = 0, 0
        cur_num, max_num = nums[0], nums[0]
        for num in nums:
            if cur_num == num:
                cur_cnt += 1
            else:
                cur_num = num
                cur_cnt = 1
            if cur_cnt >= max_cnt:
                max_num = cur_num
                max_cnt = cur_cnt
        return max_num


# 9ms / 19.33MB
class SolutionDP:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            if num not in counter:
                counter[num] = nums.count(num)
            if counter[num] > len(nums) // 2:
                return num


# 53ms / 19.78MB
# n이 과반수에 해당한다면 분할 과정에서 [n,n]이 반드시 1개 이상 존재함.
class SolutionDivideConquer:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]
