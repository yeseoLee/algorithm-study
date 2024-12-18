from typing import List


# 72 ms / 27.59 MB
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                k = stack.pop()
                result[k] = i - k
            else:
                stack.append(i)
        return result
