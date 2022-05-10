import sys
input = sys.stdin.readline
 
def is_lucky(str_digit):
    if sum(map(int,str_digit[:3]))==sum(map(int,str_digit[3:])):
        return True
 
t=int(input())
for i in range(t):
    str_digit = input().rstrip()
    if is_lucky(str_digit):
        print("YES")
    else:
        print("NO")
    
