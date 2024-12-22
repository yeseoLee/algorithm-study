li = list(map(int, input().split()))

asc = 0
desc = 0
for idx, val in enumerate(li):
    if idx + 1 == val:
        asc += 1
    elif idx + val == 8:
        desc += 1

if asc == 8:
    print("ascending")
elif desc == 8:
    print("descending")
else:
    print("mixed")
