n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n)]
timetable.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last = 0
for s, e in timetable:
    if last < s:
        cnt += 1
        last = e

print(cnt)
