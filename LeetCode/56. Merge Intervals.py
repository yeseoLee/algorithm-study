from typing import List


# 7ms / 21.43MB
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        prev = None
        for now in sorted(intervals, key=lambda x: (x[0], x[1])):
            if not prev:
                prev = now
                continue
            if prev[0] <= now[0] <= prev[1]:
                prev[1] = max(prev[1], now[1])
            else:
                results.append(prev)
                prev = now

        results.append(prev)
        return results
