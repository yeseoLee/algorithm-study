class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited=[False]*len(nums)
        result=[]
        
        def dfs(permutation):
            for idx,val in enumerate(nums):
                if not visited[idx]:
                    visited[idx]=True
                    dfs(permutation+[val])
                    visited[idx]=False
            if len(permutation) == len(nums):
                result.append(permutation)
         
        dfs([])
        return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        prev_elements=[]
        
        def dfs(elements):
            if len(elements)==0:
                result.append(prev_elements[:])  
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                
        dfs(nums)
        return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
