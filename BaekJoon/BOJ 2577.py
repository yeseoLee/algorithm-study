from collections import defaultdict


li = [int(input()) for _ in range(3)]

table = defaultdict(int)
for ch in str(li[0] * li[1] * li[2]):
    table[int(ch)] += 1

for i in range(10):
    print(table[i])
