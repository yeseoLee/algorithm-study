class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result=[]
        def dfs(comb,k):
            if sum(comb)==target:
                result.append(comb[:])
                return
            for i in range(k,len(candidates)):
                if sum(comb)+candidates[i]<=target:
                    dfs(comb+[candidates[i]],i)
        
        dfs([],0)
        return result
