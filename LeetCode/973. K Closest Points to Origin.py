from typing import List
import heapq


# 50ms / 22.91MB
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(i, v[0] ** 2 + v[1] ** 2) for i, v in enumerate(points)]
        distance.sort(key=lambda x: x[1])
        return [points[x[0]] for x in distance[:k]]


# 76ms / 22.62MB
class SolutionHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, x, y))

        result = []
        for _ in range(k):
            (d, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result
