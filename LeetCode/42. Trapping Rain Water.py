'''
#1.단순 배열 순회
class Solution:
    def trap(self, height: List[int]) -> int:
        def get_water(i: int,j: int):
            min_h=min(height[i],height[j])
            block=0
            for x in range(i+1,j):
                block+=height[x]
            return min_h*(j-i-1)-block        
        water=0
        i=0
        while(i<len(height)-1):
            high=i+1
            f=0
            for j in range(i+1,len(height)):
                if height[j]>=height[high] : high=j
                if height[i]<=height[j] :
                    water+=get_water(i,j)
                    i=j
                    f=1
                    break
            if f==0:
                water+=get_water(i,high)
                i=high
        return water
'''

'''
#2. 투포인터
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume=0
        left,right=0,len(height)-1
        left_max,right_max=height[left],height[right]
        while(left<right):
            left_max,right_max=max(height[left],left_max),max(height[right],right_max)
            if(height[left]<=height[right]):
                volume+=left_max-height[left]
                left+=1
            else:
                volume+=right_max-height[right]
                right-=1
        return volume
'''

'''
#3.스택
class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        volume=0
        
        for i in range(len(height)):
            while(stack and height[i]>height[stack[-1]]):
                top=stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] -1
                waters = min(height[i],height[stack[-1]]) - height[top]
                
                volume += distance * waters
            stack.append(i)
        return volume
'''
