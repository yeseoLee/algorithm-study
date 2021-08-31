class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack,result = [] , [0]*len(temperatures)
        
        for idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]: # warmer day
                tmp=stack.pop()
                result[tmp] = idx-tmp
            stack.append(idx)
        
        # no wamer day
        while stack:
            result[stack.pop()]=0
        
        return result
