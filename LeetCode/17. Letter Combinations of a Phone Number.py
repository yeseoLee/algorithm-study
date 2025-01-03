from typing import List


# 0 ms / 18.05 MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        answer = []

        def _dfs(i, letters):
            if i == len(digits):
                answer.append("".join(letters))
                return
            for letter in table[digits[i]]:
                letters.append(letter)
                _dfs(i + 1, letters)
                letters.pop()

        if digits:
            _dfs(0, [])
        return answer


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        def phone(num):
            if num == 7 or num == 9:
                num = ord("a") + (num - 2) * 3 + num // 9
                return [chr(num), chr(num + 1), chr(num + 2), chr(num + 3)]
            else:
                num = ord("a") + (num - 2) * 3 + num // 8
                return [chr(num), chr(num + 1), chr(num + 2)]

        def dfs(letters, idx):
            if idx < len(digits):
                num = int(digits[idx])
                visited[num] = True
                for letter in phone(num):
                    dfs(letters + letter, idx + 1)
                visited[num] = False
            if len(letters) != 0 and len(letters) == len(digits):
                result.append(letters)

        visited = [False] * 10
        result = []
        dfs("", 0)
        return result


# 모범답안
class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        dfs(0, "")

        return result
