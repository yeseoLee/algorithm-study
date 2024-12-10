from types import List


# 7 ms / 19.29 MB
class Solution:
    def trap(self, height: List[int]) -> int:
        # 물이 찰 때마다(=최대 높이와 크거나 같을 때마다) 비우기
        stack = []
        result = 0
        max_h = 0
        for h in height:
            if max_h <= h:
                while stack:
                    result += max_h - stack.pop()
                max_h = h
            stack.append(h)

        # 남은 스택 거꾸로 돌면서 비워주기
        # 블록이 ^ 패턴일 경우 감소하는 구간은
        # 최대 높이가 갱신되지 않아 비워지지 않기 때문
        new_stack = []
        max_h = 0
        while stack:
            h = stack.pop()
            if max_h <= h:
                while new_stack:
                    result += max_h - new_stack.pop()
                max_h = h
            new_stack.append(h)
        return result


class SolutionTwoPointer:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = (
                max(left_max, height[left]),
                max(right_max, height[right]),
            )

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


class SolutionStack:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]] - height[top])
                volume += distance * waters

            stack.append(i)
        return volume
