import re
from typing import List


# 4ms / 17.77MB
class Solution:
    def operate(self, op: str, nums1: list[int], nums2: list[int]) -> list[int]:
        # mapping str:func
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }
        return [ops[op](num1, num2) for num2 in nums2 for num1 in nums1]

    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = re.split(r"[+\-*]", expression)
        if len(nums) == 1:
            return [int(nums[0])]

        answer, idx = [], 0
        for num in nums[:-1]:
            idx += len(num)
            a = self.diffWaysToCompute(expression[:idx])
            b = self.diffWaysToCompute(expression[idx + 1 :])
            answer.extend(self.operate(expression[idx], a, b))
            idx += 1
        return answer


# 33ms / 17.87MB
class SolutionCompact:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        results = []
        for idx, val in enumerate(expression):
            if val in "-+*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1 :])

                result = [eval(str(l) + val + str(r)) for r in right for l in left]
                results.extend(result)
        return results
