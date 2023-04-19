# 과제 2. 큐 함수를 이용하여 콜센터의 응답 대기 시간을 계산하시오.
        ## 단, 출력 예시와 같이 응답 대기 시간이 15분을 초과하면 "※ 잠시 후 다시 걸어주세요. (응답 대기 시간 15분 초과) ※"를 출력한 후, 
        ## 더 이상 큐에 데이터를 삽입하지 않고, 최종 대기 콜을 출력한 후 프로그램을 종료한다.

# 입력 예시: waitCall = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]
# 출력 예시
# 귀하의 대기 예상시간은 0분입니다.
# 현재 대기 콜 --> [None, None, None, None, None] 

# 귀하의 대기 예상시간은 9분입니다.
# 현재 대기 콜 --> [('사용', 9), None, None, None, None] 

# 귀하의 대기 예상시간은 12분입니다.
# 현재 대기 콜 --> [('사용', 9), ('고장', 3), None, None, None] 

# ※ 잠시 후 다시 걸어주세요. (응답 대기 시간 15분 초과) ※
# 최종 대기 콜 --> [('사용', 9), ('고장', 3), ('환불', 4), None, None] 

# 프로그램 종료!

class Queue:
    def __init__(self):
        self.size = 5
        self.queue = [ None for _ in range(self.size) ]
        self.front = -1
        self.rear = -1

    def is_queue_full(self):
        # 코드 작성 구간
        # 만약 큐 앞이 비어 있으면 한 칸 당기기
        if self.rear != self.size - 1:
          return False
        elif self.rear == self.size - 1 and self.front == -1:
          return True
        else:
          for i in range(self.front + 1, self.size):
            self.quee[i - 1] = self.queue[i]
            self.queue[False]
          self.front -= 1
          self.rear -= 1
          return False


    def is_queue_empty(self):
        # 코드 작성 구간
        if self.front == self.rear:
          return True
        else:
          return False


    def en_queue(self, data):
        # 코드 작성 구간
        if self.is_queue_full():
          return
        self.rear += 1
        self.queue[self.rear] = data


    def calc_time(self):
        # 코드 작성 구간
        sum = 0
        while self.rear == None:
         pass 
        return sum
          




test_queue = Queue()
waitCall = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]


## 출력 예시
    ## 귀하의 대기 예상시간은 9분입니다.
    ## 현재 대기 콜 -->  [('사용', 9), None, None, None, None]

    ## ※ 잠시 후 다시 걸어주세요. (응답 대기 시간 15분 초과) ※
    ## 최종 대기 콜 --> [('사용', 9), ('고장', 3), ('환불', 4), None, None]

# 코드 작성 구간
print('귀하의 대기 예상시간은 ', test_queue.calc_time(),'분 입니다.')
for i in range(5):
  test_queue.en_queue(waitCall[i])
  if test_queue.calc_time() < 15:
    print('현재 대기 콜 -->  ', test_queue.queue)
    print('귀하의 대기 예상시간은 ', test_queue.calc_time(),'분 입니다.')
  else:
    print('※ 잠시 후 다시 걸어주세요. (응답 대기 시간 15분 초과) ※')
    print('최종 대기 콜 --> ', test_queue.queue)
