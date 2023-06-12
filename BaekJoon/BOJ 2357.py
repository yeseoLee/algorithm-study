# BOJ 2357 최솟값과 최댓값 골드1

import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
pair = [map(int, input().split()) for _ in range(M)]

# logic


class SegmentTree():
    def __init__(self, arr):
        self.n = len(arr)
        self.mintree = [0]*(4*self.n)
        self.maxtree = [0]*(4*self.n)

        self.build_min(arr, 0, self.n-1, 1)
        self.build_max(arr, 0, self.n-1, 1)

    def build_min(self, arr, left, right, node):
        if left == right:
            self.mintree[node] = arr[left]
            return

        mid = (left + right) // 2
        self.build_min(arr, left, mid, node*2)
        self.build_min(arr, mid+1, right, node*2+1)
        self.mintree[node] = min(self.mintree[node * 2], self.mintree[node*2+1])

    def build_max(self, arr, left, right, node):
        if left == right:
            self.maxtree[node] = arr[left]
            return

        mid = (left + right) // 2
        self.build_max(arr, left, mid, node*2)
        self.build_max(arr, mid+1, right, node*2+1)
        self.maxtree[node] = max(self.maxtree[node*2], self.maxtree[node*2+1])

    def query_min(self, left, right, node, node_left, node_right):
        if node_right < left or right < node_left: # 구간을 벗어남
            return float('inf')
        if left <= node_left and node_right <= right: # 구간 내 포함
            return self.mintree[node]

        node_mid = (node_left + node_right) // 2
        return min(self.query_min(left, right, node*2, node_left, node_mid),
                   self.query_min(left, right, node*2+1, node_mid+1, node_right))

    def query_max(self, left, right, node, node_left, node_right):
        if node_right < left or right < node_left: # 구간을 벗어남
            return 0
        if left <= node_left and node_right <= right: # 구간 내 포함
            return self.maxtree[node]

        node_mid = (node_left + node_right) // 2
        return max(self.query_max(left, right, node*2, node_left, node_mid),
                   self.query_max(left, right, node*2+1, node_mid+1, node_right))

    def get_min(self, left, right):
        return self.query_min(left, right, 1, 0, self.n-1)

    def get_max(self, left, right):
        return self.query_max(left, right, 1, 0, self.n-1)


segment_tree = SegmentTree(arr)

for a, b in pair:
    print(segment_tree.get_min(a-1, b-1), segment_tree.get_max(a-1, b-1))


''' 
시간 제한 2초인 이유
1. 일단 주어진 정수의 개수 n이 100,000이므로, O(nlog(n))의 시간복잡도 필요
2. 최댓값 세그먼트 트리, 최솟값 세그먼트 트리 2개 만들어 각각 접근
트리 접근 log(100,000) * Test Case 100,000 * 2 (최댓값, 최솟값)
=> 2nlog(n) 이므로 2 초
'''
