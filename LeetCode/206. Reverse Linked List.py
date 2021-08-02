# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#sol 1 - iterate
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node,prev = head, None
        
        while node:
            next,node.next = node.next, prev
            prev, node = node, next
        return prev

#sol 2 - recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next,node.next = node.next,prev
            return reverse(next,node)
        
        return reverse(head)
