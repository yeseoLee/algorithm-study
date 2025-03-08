from typing import List


# 0ms / 19.03MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        now_p = prices[0]

        for i, p in enumerate(prices, 1):
            if now_p < p:
                profit += p - now_p
            now_p = p

        return profit
