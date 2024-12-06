# 364 ms / 17.33 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = s[0]
        for i in range(1, len(s)):
            # 짝수
            l, r = i - 1, i
            while True:
                if l < 0 or r >= len(s):
                    break
                if s[l] != s[r]:
                    break
                if len(answer) < r + 1 - l:
                    answer = s[l : r + 1]
                l -= 1
                r += 1
            # 홀수
            l, r = i - 1, i + 1
            while True:
                if l < 0 or r >= len(s):
                    break
                if s[l] != s[r]:
                    break
                if len(answer) < r + 1 - l:
                    answer = s[l : r + 1]
                l -= 1
                r += 1

        return answer
