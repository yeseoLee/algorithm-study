💡 스택 (Stack)
📌 Stack 정의
스택은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있도록 제한된 선형으로 나열된 자료구조이다. 쉽게 비유하자면 비어있는 '프링글스 통'을 생각해보자. 과자를 먹을 때, 맨 위에 있는 과자부터 먹을 수 있고, 새로 과자를 추가한다면 먼저 들어간 과자보다 위에 쌓이는 형태일 것이다.

스택은 가장 먼저 들어간 자료가 맨 아래쪽에 쌓이고, 가장 나중에 들어간 자료가 맨 위에 쌓이기 때문에, 먼저 들어간 자료일 수록 나중에 나오고, 늦게 들어갈 수록 더 빨리 나온다.
이를 후입선출 구조라고 하고, 영어로는 LIFO : Last In First Out 라고 한다.

📌 Stack 기본연산
push()
스택에 원소를 추가한다.
pop()
스택 가장 위에 있는 원소를 삭제하고 그 원소를 반환한다.
peek()
스택 가장 위에 있는 원소를 반환한다. (삭제하지는 않는다.)
empty()
스택이 비어있다면 1, 아니면 0을 반환한다.
📌 Stack 구현
파이썬에서는 스택을 리스트 또는 연결리스트로 구현한다.
파이썬은 C언어와 다르게 단순 리스트로 구현할 수 있는 이유가 끝내주는 내장함수를 제공한다. S.append() 리스트 맨 끝에 원소를 추가한다. 시간복잡도는 O(1)이다.
S.pop(i) 리스트의 i번째 원소를 삭제한다. S.pop(-1)은 맨 앞에 있는 원소를 삭제한다. 시간복잡도는 마찬가지로 O(1)이다.

다음은 가장 기본의 연산을 가지는 스택이다.


class Stack:
    #리스트를 이용한 스택 구현
    def __init__(self):
        self.top = []
    #스택 크기 반환
    def __len__(self) -> bool :
        return len(self.top)
    
    #구현함수
    #스택에 원소 삽입
    def push(self, item):
        self.top.append(item)
    #스택 가장 위에 있는 원소를 삭제하고 반환   
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()
    #스택 가장 위에 있는 원소를 반환
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()
    #스택이 비어있는 지를 bool값으로 반환
    def isEmpty(self) -> bool :
        return len(self.top)==0
다음은 기본 연산을 확장한 스택이다.

class Stack:
    #리스트를 이용하여 스택 생성
    def __init__(self, limit: int= 100):
        self.top = []
        self.limit = limit
    #스택 크기 반환
    def __len__(self) -> bool :
        return len(self.top)
    #스택 내부 자료 전체를 string으로 변환하여 반환
    def __str__(self) -> str :
        return str(self.top[::1])

    #구현함수
    #스택에 원소 삽입
    def push(self, item):
        if(len(self.pop)>=self.limit):
            self.top.append(item)
    #스택 가장 위에 있는 원소를 삭제하고 반환
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()
    #스택 가장 위에 있는 원소를 반환
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()
    #스택을 비움
    def clear(self):
        self.top=[]
    #스택 안에 특정 item이 포함되어 있는지를 bool값으로 반환
    def isContain(self, item) -> bool:
        return item in self.top
    #스택이 비어있는 지를 bool값으로 반환
    def isEmpty(self) -> bool :
        return len(self.top)==0
    #스택이 가득 차 있는 지를 bool값으로 반환
    def isFull(self) -> bool :
        return self.size()==self.limit
    #스택의 크기를 int 값으로 반환 
    def size(self) -> int :
        return len(self.top)
📌 Stack 라이브러리
파이썬 내장모듈에서는 따로 스택 라이브러리가 존재하지 않는다.
보통 덱 라이브러리를 import 해서 스택 대신 사용한다.

from collections import deque

dq=deque() # 덱 생성
dq.append() # 덱의 가장 왼쪽에 원소 삽입
dq.popleft() # 가장 왼쪽 원소 반환
dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입
dp.pop() # 가장 오른쪽 원소 반환
dp.clear() # 모든 원소 제거
dp.copy() # 덱 복사
dp.count(x) #x와 같은 원소의 개수를 계산
'''공식문서 : https://docs.python.org/3.8/library/collections.html#collections.deque'''