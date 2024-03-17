# BOJ 15829 hashing 브론즈 2

L = int(input())
S = input().rstrip()

r, m = 31, 1234567891
letter_idx = {}
for i in range(26):
    letter_idx[chr(ord('a')+i)] = i+1


def hash(s: str) -> int:
    li = list(s)
    result = 0
    for i, v in enumerate(li):
        result = (result + letter_idx[v] * r**i) % m
    return result


print(hash(S))
