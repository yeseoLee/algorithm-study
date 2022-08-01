# BOJ 1208
import sys
import bisect

# input
input = sys.stdin.readline
n, s = map(int, input().split())
input_arr = list(map(int, input().split()))

# init
left_arr, right_arr = input_arr[:n//2], input_arr[n//2:]
left_part, right_part = [], []
result = 0

# logic
def get_part(idx, sum, arr, is_left):
    global result
    if idx >= len(arr):
        return
    sum += arr[idx]
    if sum == s:
        result += 1
    if is_left:
        left_part.append(sum)
    else:
        right_part.append(sum)
    get_part(idx+1, sum-arr[idx], arr, is_left)
    get_part(idx+1, sum, arr, is_left)

def find_number(num, arr):
    return bisect.bisect_right(arr, num) - bisect.bisect_left(arr, num)

get_part(0, 0, left_arr, True)
get_part(0, 0, right_arr, False)

left_part.sort()
right_part.sort()

for i in left_part:
    result += find_number(s-i, right_part)

# output
print(result)

'''
# TIME LIMIT
import sys

# input
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# init
acc = arr[:]
for i in range(1, n):
    acc[i] += acc[i-1]

# logic
result = 0
def backtracking(x, acc):
    global result
    if (x != 0 and acc == s):
        result += 1
    for i in range(x, n):
        acc += arr[i]
        backtracking(i+1, acc)
        acc -= arr[i]

# output
backtracking(0, 0)
print(result)
'''
