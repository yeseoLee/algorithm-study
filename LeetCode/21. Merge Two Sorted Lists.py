from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 3ms / 17.31 MB
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        node1 = list1
        node2 = list2

        merged_list = ListNode()
        merged_node = merged_list

        while node1 and node2:
            if node1.val < node2.val:
                merged_node.val = node1.val
                node1 = node1.next
            else:
                merged_node.val = node2.val
                node2 = node2.next
            if node1 or node2:
                merged_node.next = ListNode()
                merged_node = merged_node.next

        while node1:
            merged_node.val = node1.val
            node1 = node1.next
            if node1:
                merged_node.next = ListNode()
                merged_node = merged_node.next

        while node2:
            merged_node.val = node2.val
            node2 = node2.next
            if node2:
                merged_node.next = ListNode()
                merged_node = merged_node.next

        return merged_list
