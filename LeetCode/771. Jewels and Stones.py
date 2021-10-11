#collections.Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_counter = collections.Counter(stones)
        cnt=0
        for jewel in jewels:
            cnt+=stone_counter[jewel]
        return cnt

#Pythonic Way
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
