'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        left=[1]*n
        right=[1]*n
        for i in range(1,n):
            left[i]*=left[i-1]*nums[i-1]
            right[n-i-1]*=right[n-i]*nums[n-i]
        for i in range(n):
            answer[i]=left[i]*right[i]
        return answer
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        p=1
        #left
        for i in range(len(nums)):
            out.append(p)
            p*=nums[i]
        p=1
        #right
        for i in range(len(nums)-1,-1,-1):
            out[i]*=p
            p*=nums[i]
        return out
