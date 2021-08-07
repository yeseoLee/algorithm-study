# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Swap value
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node=head
        while(node and node.next):
            node.val,node.next.val=node.next.val,node.val
            node=node.next.next
        return head

#Swap Node
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root=prev=ListNode(None)
        prev.next=head
        while head and head.next:
            #교환 (prev->head->next 에서 prev->next->head)
            next = head.next
            head.next = next.next
            next.next=head
            prev.next=next
            #이동
            head = head.next
            prev = prev.next.next
        
        return root.next

#recursive
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
