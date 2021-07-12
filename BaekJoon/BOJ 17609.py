from collections import deque
def is_palindrome(s: str):
    return s==s[::-1]

def is_pal_or_pseudo(s : str):
    left=0
    right=len(s)-1
    while(left<right):
        if(s[left]!=s[right]):
            if(left+1==right):
                return 1
            if is_palindrome(s[left+1:right+1]): #delete left char
                return 1
            if is_palindrome(s[left:right]): #delete right char
                return 1
            return 2
        left+=1
        right-=1
    return 0
    
t=int(input())
for i in range(t):
    s=input()        
    print(is_pal_or_pseudo(s))

'''
print(left,right)
print(s[left+1:right+1])
print(s[left:right])
'''
