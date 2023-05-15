# BOJ 1039 교환 골드 3

N, K = input().split()
K = int(K)
li = list(map(int, N))

if len(li) == 1 or sum(li) == li[0]:
    print(-1)
    exit(0)

k = min(K, len(li))
count = 0
for i in range(k):
    max_idx = i
    for j in range(i+1, len(li)):
        if li[j] >= li[max_idx]:
            max_idx = j
    if max_idx == i:
        break
    li[i], li[max_idx] = li[max_idx], li[i]
    count += 1

if (k-count) % 2 == 1:
    li[len(li)-1], li[len(li)-2] = li[len(li)-2], li[len(li)-1]

print(''.join(map(str, li)))
