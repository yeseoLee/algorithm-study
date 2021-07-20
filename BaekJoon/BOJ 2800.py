from itertools import combinations
def print_susik(x):
    ans=set()
    for i in range(1,len(x)+1):
        for j in combinations(x,i):
            new_susik=susik[:]
            for left,right in j:
                new_susik[left],new_susik[right]='',''
            ans.add(''.join(new_susik))
    for i in sorted(ans):
        print(i)

#입력
susik=list(input())

#괄호 구하기
stack=[]
parentheses=[]
for idx,val in enumerate(susik):
    if(val=='('):
        stack.append(idx)
    elif(val==')'):
        parentheses.append([stack.pop(),idx])

#괄호 제거
print_susik(parentheses)


'''
계속 ans=[] list로 풀어서 실패했다...
원인은 ((0)) 같이 괄호가 두번 감싸져 있는 경우는
겹치는 Case 가 발생하기 때문에 집합을 사용해야 한다.
ans=set() !!!
'''
