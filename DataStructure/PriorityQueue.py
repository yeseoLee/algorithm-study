#클래스 불러오기
from queue import PriorityQueue

#우선순위 큐 생성
que = PriorityQueue()
#limitedQue = PriorityQueue(maxsize=10)

#원소 삽입 - 정수
que.put(item)
que.put(1)
que.put(2)
#원소 삽입 - 튜플
que.put((priority, item))
que.put((2,'hello'))
que.put((1,'world'))
#원소 삭제 및 반환
print(que.get())



