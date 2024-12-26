from typing import List
from collections import Counter


# 5 ms / 21.30 MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        answer = [key for key, val in counter.most_common(k)]
        return answer


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        result = []
        for val, cnt in counter.most_common():
            result.append(val)
        return result[:k]


class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]
