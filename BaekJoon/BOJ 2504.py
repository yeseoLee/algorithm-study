line=input().rstrip()
stack=[]
result=0
def check(line):
    stack = []
    flag = True
 
    for i in line:
        if i == '(' or i == '[':
            stack.append(i)
 
        else:
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
 
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
 
    if not stack and flag:
        return True
    return False

if not check(line):
    print(0)
else:
    for i in line:
        if i==')':
            tmp=1
            while stack:
                top = stack.pop()
                if top=='(':
                    stack.append(tmp*2)
                    break
                else:
                    if tmp==1:
                        tmp = top
                    else:
                        tmp += top
        elif i==']':
            tmp=1
            while stack:
                top = stack.pop()
                if top=='[':
                    stack.append(tmp*3)
                    tmp=1
                    break
                else:
                    if tmp==1:
                        tmp = top
                    else:
                        tmp += top
        else:
            stack.append(i)
    print(sum(stack))

