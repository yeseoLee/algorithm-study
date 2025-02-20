from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.idx = -1
        self.palindrome_idxs = []
        self.children = defaultdict(TrieNode)


# 3870ms / 609.01MB
class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, word: str, idx: int):
        node = self.root
        for i, ch in enumerate(reversed(word)):
            if self.is_palindrome(word[: len(word) - i]):
                node.palindrome_idxs.append(idx)
            node = node.children[ch]
        node.idx = idx

    def search(self, word: str, idx: int):
        result = []
        node = self.root
        while word:
            if node.idx >= 0:
                if self.is_palindrome(word):
                    result.append([idx, node.idx])
            if not word[0] and node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        if node.idx >= 0 and node.idx != idx:
            result.append([idx, node.idx])

        for palindrome_idx in node.palindrome_idxs:
            result.append([idx, palindrome_idx])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for idx, word in enumerate(words):
            trie.insert(word, idx)

        answer = []
        for idx, word in enumerate(words):
            answer.extend(trie.search(word, idx))
        return answer
