class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        def dfs(subset,k):
            for i in range(k,len(nums)):
                dfs(subset+[nums[i]],i+1)
            result.append(subset)
        
        dfs([],0)
        return result
