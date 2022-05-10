class Stack:
    #리스트를 이용하여 스택 생성
    def __init__(self, limit: int= 100):
        self.top = []
        self.limit = limit
    #스택 크기 반환
    def __len__(self) -> bool :
        return len(self.top)
    #스택 내부 자료를 string으로 변환하여 반환
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
