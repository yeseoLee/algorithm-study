class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while a != 0:
            a, b = ((a & b) << 1) & MASK, (a ^ b) & MASK

        if b > INT_MAX:
            b = ~(b ^ MASK)
        return b
