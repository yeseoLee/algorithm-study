from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 4 ms / 17.29 MB
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        answer = ListNode()
        n = answer
        temp = 0

        n1, n2 = l1, l2
        while True:
            if not (n1 or n2):
                if temp != 0:
                    newnode = ListNode(val=temp)
                    n.next = newnode
                break
            newnode = ListNode()
            n.next = newnode
            n = n.next
            if not n1:
                num = temp + n2.val
                n2 = n2.next
            elif not n2:
                num = temp + n1.val
                n1 = n1.next
            else:
                num = temp + n1.val + n2.val
                n1 = n1.next
                n2 = n2.next

            if num >= 10:
                temp = 1
                n.val = num - 10
            else:
                n.val = num
                temp = 0

        return answer.next
