# BOJ 5639 골드4 이진 검색 트리 https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


def postorder(left, right):
    if left > right:
        return
    mid = right + 1  # 루트보다 큰 값이 존재하지 않을 경우
    for i in range(left + 1, right + 1):
        if arr[left] < arr[i]:
            mid = i
            break

    # left subtree, right subtree, root
    postorder(left + 1, mid - 1)
    postorder(mid, right)
    print(arr[left])


postorder(0, len(arr) - 1)
