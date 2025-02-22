from typing import List


# 0ms / 18.30MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1

        # 경계 찾기
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid
        k = l

        # 이진 탐색 1
        l, r = 0, k
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                answer = mid
                break

        if answer != -1:
            return answer

        # 이진 탐색 2
        l, r = k + 1, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                answer = mid
                break

        return answer
