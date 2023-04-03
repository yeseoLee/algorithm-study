# 과제 1. 스택함수를 이용하여 pushed 리스트에 대해서 popped 리스트 출력결과가 발생할 수 있는지 확인하라.
# (1) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [3, 4, 5, 2, 1]
# (1) 출력 예시: True
# (1) 설명: 다음의 순서대로 push, pop 수행할 수 있으므로 True 출력
# push(1), push(2), push(3), pop() -> 3, push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 2, pop() -> 1
# (2) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [4, 5, 2, 3, 1]
# (2) 출력 예시: False
# (2) 설명: 2 은 3 이전에 pop 할 수 없음

class Stack:
    def __init__(self):
        self.size = 10
        self.stack = [ None for _ in range(self.size) ]
        self.top = -1

    def is_stack_full(self):
        # 코드 작성 구간
        if self.top >= self.size - 1:
          return True
        else:
          return False


    def is_stack_empty(self):
        # 코드 작성 구간
        if self.top == -1:
          return True
        else:
          return False


    def push(self, data):
        # 코드 작성 구간
        if self.is_stack_full():
          return
        self.top += 1
        self.stack[self.top] = data


    def pop(self):
        # 코드 작성 구간
        if self.is_stack_empty():
          return None
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data


    def peek(self):
        # 코드 작성 구간
        if self.is_stack_empty():
          return None
        return self.stack[self.top]


    def validate_stack_sequences(self, pushed, popped):
        # 코드 작성 구간
        i = 0 # pushed를 순회하는 인덱스
        j = 0 # popped를 순회하는 인덱스
        procedure = '' # 진행 과정을 기록하는 변수

        # pushed 배열을 전부 순회하며 popped각 원소와 비교
        while i<len(pushed) and j<len(popped):
            if pushed[i] != popped[j]:
                self.push(pushed[i])
                i+=1
            else:
               i+=1
               j+=1

        # case 1. j==len(popped) popped 배열과 pushed 배열을 전부 순회하여 사용함
        if j==len(popped):
            return True
        # case 2. i==len(pushed) popped배열에 아직 비교하지 않은 원소가 남아있는 경우
        for j in range(j, len(popped)):
          if popped[j] != self.pop():
            return False
        return True
          
# 실행 구문 (아래 코드를 수정하지 마시오.)
test_stack = Stack()

pushed = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
popped = [[3, 4, 5, 2, 1], [4, 5, 2, 3, 1], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]]

for i in range(len(pushed)):
    print(test_stack.validate_stack_sequences(pushed[i], popped[i]))
