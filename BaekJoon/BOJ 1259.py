# BOJ 1259 펠린드롬수 브론즈 1

def is_palindrome(li: list) -> bool:
    if len(li) <= 1:
        return True
    return li[0] == li[-1] and is_palindrome(li[1:-1])


while (True):
    n = input().rstrip()
    if n == '0':
        break
    if is_palindrome(list(n)):
        print("yes")
    else:
        print("no")
