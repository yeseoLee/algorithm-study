n = int(input())
li = list(map(int, input().split()))  # 6
t, p = map(int, input().split())

answer_t = 0
for v in li:
    if v % t == 0:
        answer_t += v // t
    else:
        answer_t += v // t + 1

print(answer_t)
print(*divmod(n, p))
