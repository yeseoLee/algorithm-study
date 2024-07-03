def solution(s):
    answer = True
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if len(stack) == 0 or not stack[-1] == "(":
                return False
            stack.pop()
    return len(stack) == 0
