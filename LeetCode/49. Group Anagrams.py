from collections import defaultdict
from types import List


def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams["".join(sorted(word))].append(word)
    return list(anagrams.values())


# 11 ms / 20.23 MB
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            anagram = "".join(sorted(list(s)))
            anagram_dict[anagram].append(s)
        return list(anagram_dict.values())
