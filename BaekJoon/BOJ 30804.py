from collections import Counter
import sys


input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s, e = 0, -1
answer = 0
counter = Counter()

while e < n - 1:
    e += 1
    counter[arr[e]] += 1
    if len(counter) <= 2:
        answer = max(answer, e - s + 1)
    while s <= e and len(counter) > 2:
        counter[arr[s]] -= 1
        if counter[arr[s]] == 0:
            del counter[arr[s]]
        s += 1

print(answer)
