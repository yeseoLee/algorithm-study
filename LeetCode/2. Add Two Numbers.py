# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1,n2=l1,l2
        f=0
        while(1):
            sum=(n1.val+n2.val+f)
            f=sum//10
            n1.val= sum%10
            if n1.next and n2.next:
                pass
            elif n1.next:
                n2.next=ListNode(0)
            elif n2.next:
                n1.next=ListNode(0)
            else:
                if f: n1.next=ListNode(1)
                break
            n1,n2=n1.next,n2.next
        return l1

#2.전가산기 (풀이 1의 개선)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry,val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next

#3.파이썬 리스트
class Solution:
    # 연결 리스트를 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev =head, None
        while node:
            next, node.next =node.next,prev
            prev, node = node, next
        return prev
    
    # 연결리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    # 파이썬 리스트를 연결리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node       
        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        
        #최종 계산 결과 연결 리스트 반환
        return self.toReversedLinkedList(str(resultStr))
        
