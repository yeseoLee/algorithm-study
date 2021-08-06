# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #예외처리
        if not (head and head.next):
            return head
        #짝수 리스트 저장
        e_list=head.next
        #짝수끼리/홀수끼리 연결
        odd,even=head,head.next
        while(even and even.next):
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        #합해서 반환
        odd.next=e_list
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #예외처리
        if head is None:
            return None
        
        odd=head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next, even.next = odd.next.next,even.next.next
            odd,even = odd.next, even.next
        
        odd.next = even_head
        return head
