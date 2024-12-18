class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for ch in list(s):
            if ch not in ch_map:
                stack.append(ch)
            else:
                if not stack or ch_map[ch] != stack.pop():
                    return False
        return len(stack) == 0
