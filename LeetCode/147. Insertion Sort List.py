from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 555ms / 18.77MB
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        sorted_head = ListNode()
        sorted_head.next = ListNode(head.val)

        sorted_node = sorted_head
        node = head
        while node.next:
            if not sorted_node.next:
                sorted_node.next = node.next
                node.next = node.next.next
                sorted_node.next.next = None
                sorted_node = sorted_head
            elif node.next.val > sorted_node.next.val:
                sorted_node = sorted_node.next
            else:
                sorted_node_next = sorted_node.next
                sorted_node.next = node.next
                node.next = node.next.next
                sorted_node.next.next = sorted_node_next
                sorted_node = sorted_head

        return sorted_head.next
