#1. recursive

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters=sorted(set(s))
        
        for letter in letters:
            suffix = list(s[s.index(letter):])
            suffix=[letter]+[x for x in suffix if x!=letter]
            
            if set(suffix) == set(s):
                return letter + self.removeDuplicateLetters(suffix[1:])
            
        return ""

#1-1
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for letter in sorted(set(s)):
            suffix = s[s.index(letter):]
            if set(suffix) == set(s):
                return letter + self.removeDuplicateLetters(suffix.replace(letter, ''))
        return ''

#2. stack

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        
        for char in s:
            counter[char] -=1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
            
        return ''.join(stack)
