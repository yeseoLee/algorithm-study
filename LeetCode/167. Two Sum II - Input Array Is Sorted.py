from typing import List


# 39ms / 18.78MB
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers) - 1):
            t = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                j = l + (r - l) // 2
                if numbers[j] < t:
                    l = j + 1
                elif numbers[j] > t:
                    r = j - 1
                else:
                    return [i + 1, j + 1]
