import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


inorder_idxs = [0] * (n + 1)
for i in range(n):
    inorder_idxs[inorder[i]] = i


# inorder에서 루트 노드를 찾기 위함. 1~n 사이 값의 노드만 존재하기 때문에
def get_inorder_idx(root):
    return inorder_idxs[root]


def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return

    # postorder에서 루트 노드 획득
    root = postorder[postEnd]

    # inorder에서 루트 노드의 위치를 통해 왼쪽 서브 트리 개수와 오른쪽 서브트리 개수를 파악
    leftNode = get_inorder_idx(root) - inStart
    rightNode = inEnd - get_inorder_idx(root)

    # preorder 출력: root -> left -> right
    # inorder은 중간에 root, postorder는 맨 마지막에 root가 있기 떄문에 이를 반영하여 작성
    print(root, end=" ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)


preorder(0, n - 1, 0, n - 1)
