# 12ms / 18.75MB
class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True

        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True

        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
