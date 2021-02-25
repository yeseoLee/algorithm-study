from collections import deque
line=input()
operator=['+','-','*','/','(',')'] #연산자
stack=deque() 
for i in line:
    if(i in operator): #연산자일 때
        #우선순위가 낮은 연산자 -> 앞선 연산들을 전부 출력
        if(i=='+' or i=='-'):
            while(stack):
                #괄호 내에 있는 연산이였을 때는 괄호 내 연산자만 출력
                if(stack[-1]=='('): 
                    break
                print(stack.pop(),end="")
            stack.append(i)
        #'*','/' 우선순위가 높은 연산자들은 먼저 나온 애들 먼저 출력
        elif(i=='*' or i=='/'):
            if(len(stack)!=0 and (stack[-1]=='*' or stack[-1]=='/')):
                print(stack.pop(),end="")
            stack.append(i)
        #열린 괄호는 stack에 push만
        elif(i=='('):
            stack.append(i)
        #닫힌 괄호가 나오면 괄호 내 모든 연산을 출력해준다.
        else:
            while(stack[-1]!='('):
                print(stack.pop(),end="")
            stack.pop()
    else:
        print(i,end="")

while(stack):
    print(stack.pop(),end="")
