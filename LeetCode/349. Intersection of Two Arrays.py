import bisect
from typing import List


# 3ms / 17.86MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))

        for num in nums1:
            i = bisect.bisect_left(nums2, num)
            if i < len(nums2) and nums2[i] == num:
                result.append(num)

        return result
