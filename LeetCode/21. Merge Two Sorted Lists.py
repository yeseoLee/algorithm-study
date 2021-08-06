# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode()
        now=l3
        n1,n2=l1,l2
        while(1):
            if n1==None and n2==None:
                return l3.next
            elif n2==None:
                while(n1!=None):
                    newnode=ListNode(n1.val)
                    now.next=newnode
                    now=now.next
                    n1=n1.next
            elif n1==None:
                while(n2!=None):
                    newnode=ListNode(n2.val)
                    now.next=newnode
                    now=now.next
                    n2=n2.next
            else:
                if n1.val < n2.val:
                    newnode=ListNode(n1.val)
                    now.next=newnode
                    now=now.next
                    n1=n1.next
                else:
                    newnode=ListNode(n2.val)
                    now.next=newnode
                    now=now.next
                    n2=n2.next
        return l3.next
