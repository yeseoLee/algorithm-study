import sys 
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [int(input()) for _ in range(N)]
command = [list(map(int,input().split())) for _ in range(M)]


class SegmentTree:
    def __init__(self,arr):
        self.n = len(arr)
        self.tree = [0]*(self.n*4)
        
        self.build(arr,0,self.n-1, 1)
    
    def build(self,arr,left,right,node):
        if left==right:
            self.tree[node] = arr[left]
            return
        
        mid = (left+right) // 2
        self.build(arr, left, mid, node*2)
        self.build(arr, mid+1, right, node*2+1)
        self.tree[node] = min(self.tree[node*2], self.tree[node*2+1])
    
    def get_min(self, left,right, node, node_left,node_right):
        # out of range
        if node_right < left or right < node_left:
            return float('inf')
        # include
        if left <= node_left and node_right <= right:
            return self.tree[node]
        
        # in range
        node_mid = (node_left + node_right) // 2
        return min(self.get_min(left, right, node*2, node_left, node_mid),
                   self.get_min(left,right,node*2+1, node_mid+1, node_right))
    
    def update(self, left, right, node, index, diff):
        if index < left or index > right:
            return
        self.tree[index] = diff
        if left == right: #leaf node
            return
        mid = (left+right)//2
        self.update(left, mid, node*2, index, diff)
        self.update(mid+1, right, node*2+1, index, diff)
        self.tree[node] = min(self.tree[node*2] , self.tree[node*2+1])

segment_tree = SegmentTree(arr)
for a,b in command:
    print(segment_tree.get_min(a-1, b-1, 1, 0, segment_tree.n-1))
