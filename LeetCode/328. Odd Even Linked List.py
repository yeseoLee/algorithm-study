from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 0 ms / 18.95 MB
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head, even_head = head, head.next
        odd, even = odd_head, even_head
        while True:
            odd.next = odd.next.next if odd.next and odd.next.next else None
            odd = odd.next if odd.next else odd
            even.next = even.next.next if even.next and even.next.next else None
            even = even.next if even.next else even

            if not (odd.next and even.next):
                break

        odd.next = even_head
        return odd_head
