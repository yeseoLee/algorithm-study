class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # result = 0
        # for ch in bin(x ^ y):
        #     if ch=="1":
        #         result += 1
        # return result
        return bin(x ^ y).count("1")
