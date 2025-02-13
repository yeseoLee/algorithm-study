import heapq
from typing import List


class Solution:
    # 203ms / 34.99MB
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, (-num, num))
        for i in range(k - 1):
            heapq.heappop(h)
        return heapq.heappop(h)[1]

    # 54ms / 28.75MB
    def findKthLargestwithSort(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]
