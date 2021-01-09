class Stack:
    #리스트를 이용하여 스택 생성
    def __init__(self, limit: int= 100):
        self.top = []
        self.limit = limit
    #스택 크기 출력
    def __len__(self) -> bool :
        return len(self.top)
    #스택 내부 자료를 string으로 변환하여 반환
    def __str__(self) -> str :
        return str(self.top[::1])

    #구현함수
    def push(self, item):
        if(len(self.pop)>=self.limit):
            self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()
    def clear(self):
        self.top=[]
    def isContain(selff, item) -> bool:
        return item in self.top
    def isEmpty(self) -> bool :
        return len(self.top)==0
    def isFull(self) -> bool :
        return self.size()==self.limit
    def size(sellf) -> int :
        return len(self.top)
