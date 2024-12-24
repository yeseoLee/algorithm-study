from collections import defaultdict


# 0 ms / 17.87 MB
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_table = defaultdict(int)
        for stone in stones:
            stone_table[stone] += 1

        answer = 0
        for jewel in jewels:
            answer += stone_table[jewel]
        return answer
