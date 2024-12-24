# 964ms / 177.52 MB
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.k = 23
        self.hash = [None] * self.size

    def put(self, key: int, value: int) -> None:
        if not self.hash[(key + self.k) % self.size]:
            self.hash[(key + self.k) % self.size] = Node(key, value)

        node = self.hash[(key + self.k) % self.size]
        while node:
            if node.key == key:
                node.val = value
                return
            node = node.next
        node = Node(key, value)

    def get(self, key: int) -> int:
        node = self.hash[(key + self.k) % self.size]
        while node:
            if node.key == key:
                return node.val
        return -1

    def remove(self, key: int) -> None:
        node = self.hash[(key + self.k) % self.size]
        if not node or not node.next:
            self.hash[(key + self.k) % self.size] = None
            return

        prev = node
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev = node
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
