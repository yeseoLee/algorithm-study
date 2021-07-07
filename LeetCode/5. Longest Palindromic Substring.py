
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substring = ''
        len_max = 0
        if(len(s) < 2 or s == s[::-1]):
            return s
        for i in range(1, len(s)):
            if(s[i-1] == s[i]):  # even
                left = i-1
                right = i
                while(1):
                    if(left < 0 or right >= len(s)):
                        break
                    if(right-left+1 > len_max and s[left:right+1] == s[left:right+1][::-1]):
                        max_substring = s[left:right+1]
                        len_max = right-left+1
                    left -= 1
                    right += 1
            if(i+1 < len(s) and s[i-1] == s[i+1]):  # odd
                left = i-1
                right = i+1
                while(1):
                    if(left < 0 or right >= len(s)):
                        break
                    if(right-left+1 > len_max and s[left:right+1] == s[left:right+1][::-1]):
                        max_substring = s[left:right+1]
                        len_max = right-left+1
                    left -= 1
                    right += 1
            else:
                left, right = -1, -1
        if(len_max == 0):
            return s[0]
        return max_substring
"""