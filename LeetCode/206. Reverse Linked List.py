from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 0ms / 18.66 MB
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        node = head

        while node is not None:
            stack.append(node.val)
            node = node.next
        reversed_head = ListNode()
        node = reversed_head

        while stack:
            node.val = stack.pop()
            if stack:
                node.next = ListNode()
                node = node.next

        return reversed_head
