# BOJ 11505 구간 곱 구하기 골드1
import sys
input = sys.stdin.readline

# input
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M+K)]
MOD = 1000000007

# logic


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [1] * (self.n*4)
        self.build(arr, 0, self.n-1, 1)

    def build(self, arr, left, right, node):
        if left == right:
            self.tree[node] = arr[left] % MOD
            return

        mid = (left+right) // 2
        self.build(arr, left, mid, node*2)
        self.build(arr, mid+1, right, node*2+1)
        self.tree[node] = (self.tree[node*2] * self.tree[node*2+1]) % MOD

    def update(self, left, right, node, index, diff):
        if (index < left or right < index):  # out of range
            return
        # in range
        self.tree[node] = diff % MOD
        if (left == right):  # leaf node
            return
        # not leaf node
        mid = (left+right) // 2
        self.update(left, mid, node*2, index, diff)
        self.update(mid+1, right, node*2+1, index, diff)
        self.tree[node] = self.tree[node*2] * self.tree[node*2+1] % MOD

    def do_update(self, index, diff):
        return self.update(0, self.n-1, 1, index, diff)

    def query(self, left, right, node, node_left, node_right):
        if node_right < left or right < node_left:  # out of range
            return 1
        if left <= node_left and node_right <= right: # in range
            return self.tree[node]
        node_mid = (node_left + node_right) // 2

        return self.query(left, right, node*2, node_left, node_mid) * self.query(left, right, node*2+1, node_mid+1, node_right) % MOD

    def get_product(self, left, right):
        return self.query(left, right, 1, 0, self.n-1)


# output
segment_tree = SegmentTree(arr)

for a, b, c in commands:
    if a == 1:
        segment_tree.do_update(b-1, c)
    elif a == 2:
        print(segment_tree.get_product(b-1, c-1))
