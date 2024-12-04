from typing import List


# 0 ms / 22.5 MB
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # l,r = 0, len(s)-1
        # while l<r:
        #     s[l],s[r] = s[r],s[l]
        #     l+=1
        #     r-=1
