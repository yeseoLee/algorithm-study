# BOJ 10610
import sys
input = sys.stdin.readline
num_list = list(map(int, input().rstrip()))
def logic():
    if 0 in num_list and sum(num_list) % 3 == 0:
        num_list.sort(reverse=True)
        return ''.join(map(str, num_list))
    else:
        return -1
print(logic())
