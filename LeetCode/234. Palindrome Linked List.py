from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 21ms / 38.85 MB
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        node = head
        while node is not None:
            arr.append(node.val)
            node = node.next
        return arr == arr[::-1]
