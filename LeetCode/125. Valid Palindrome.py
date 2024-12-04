import collections
import re


# 36ms / 15.6 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]


# 48ms / 19.2 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for char in s:
            # is char alphabet or number
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True


# 288ms / 19.6MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            # is char alphabet or number
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True


# 11ms / 18.46 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # s = [ch for ch in s if ch.isalnum()]
        # s = re.sub('[^a-z0-9]','',s)
        s = [
            ch
            for ch in s
            if ord("a") <= ord(ch) <= ord("z") or ord("0") <= ord(ch) <= ord("9")
        ]
        return s == s[::-1]
