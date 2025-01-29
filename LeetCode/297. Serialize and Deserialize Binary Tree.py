import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        queue = collections.deque([root])
        result = ["#"]
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")  # None
        return " ".join(result)

    def deserialize(self, data):
        if data == "# #":
            return None
        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] != "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# 데이터형식(string)을 맞추지 못하여 오류발생
class Codec:
    def serialize(self, root):
        if root is None:
            return ""
        serial = [root.val]
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                break
            if node.left:
                serial.append(node.left.val)
                queue.append(node.left)
            else:
                serial.append(None)
            if node.right:
                serial.append(node.right.val)
                queue.append(node.right)
            else:
                serial.append(None)
        return serial

    def deserialize(self, data):
        if len(data) == 0:
            return None
        root = TreeNode(data[0])
        queue = collections.deque([root])
        k = 1
        lr = 0
        while queue and k < len(data):
            for i in range(len(queue)):
                node = queue.popleft()
                if k >= len(data):
                    break
                if data[k]:
                    node.left = TreeNode(data[k])
                    queue.append(node.left)
                k += 1
                if k >= len(data):
                    break
                if data[k]:
                    node.right = TreeNode(data[k])
                    queue.append(node.right)
                k += 1
        return root
