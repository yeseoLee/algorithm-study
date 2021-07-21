# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        node=head
        
        while(node != None):
            arr.append(node.val)
            node = node.next
        
        #isPalindrome (Use list)
        return arr == arr[::-1]
        
        #Ispalindrome (Use Deque)
        '''
        while len(arr) > 1:
            if arr.popleft() != arr.pop():
                return False
        return True
        '''

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:        
        rev=None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            #여기 잘 이해안된다
            rev,rev.next, slow = slow, rev, slow.next
            
        if fast: #리스트가 홀수 개여서 중앙까지 이동하지 않았을 떄
            slow=slow.next
        
        #팰린드롬
        while rev and rev.val == slow.val:
            slow,rev = slow.next, rev.next
        return not rev
'''