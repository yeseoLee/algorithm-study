from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 0 ms / 17.44 MB
class SolutionSwapValue:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd, even = head, head.next
        while odd and even:
            print(odd.val, even.val)
            odd.val, even.val = even.val, odd.val
            odd = even.next if even else None
            even = odd.next if odd else None
        return head


# 0 ms / 17.15 MB
class SolutionSwapNode:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        prev, now = dummy, head
        while prev and now and now.next:
            prev.next = now.next
            now.next = now.next.next
            prev.next.next = now

            prev = now
            now = now.next

        return dummy.next
