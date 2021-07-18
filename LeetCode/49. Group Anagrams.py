import collections
def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        separate = []
        for i in range(len(strs)):
            if(strs[i] == -1):
                continue
            tmp = sorted(list(strs[i]))
            x = [strs[i]]
            for j in range(i+1, len(strs)):
                if(strs[j] == -1):
                    continue
                if(sorted(list(strs[j])) == tmp):
                    x.append(strs[j])
                    strs[j] = -1
            separate.append(x)
        return separate
"""
