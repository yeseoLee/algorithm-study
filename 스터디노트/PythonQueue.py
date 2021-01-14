from queue import Queue
from collections import deque

"""Queue
que=queue.Queue(maxsize) #maxsize의 기본값은 0(무한)
que.qsize() #큐의 아이템 개수를 반환
que.put(item) #아이템을 큐에 삽입
que.get() #가장 먼저 들어간 아이템 반환
que.empty() #큐가 비어있는지 참/거짓 반환 
que.full() #큐가 가득 차있는지 참/거짓 반환
https://docs.python.org/3/library/queue.html
"""

q=Queue(5) #최대크기 5의 큐 생성
print(q)
for i in range(5): 
    q.put(i)
print(q.qsize())
print(q.full())
for i in range(5): 
    print(q.get(),end="")
print("")
print(q.empty())

"""deque
dq=deque()
dq.append() # 덱의 가장 왼쪽에 원소 삽입
dq.popleft() # 가장 왼쪽 원소 반환
dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입
dp.pop() # 가장 오른쪽 원소 반환
dp.clear() # 모든 원소 제거
dp.copy() # 덱 복사
dp.count(x) #x와 같은 원소의 개수를 계산
https://docs.python.org/3.8/library/collections.html#collections.deque
"""
dq=deque([3,4,5])

dq.appendleft(2)
print(dq) #deque([2,3,4,5])
dq.appendleft(1)
print(dq) #deque([1,2,3,4,5])

print(dq.pop()) # 5
print(dq.pop()) # 4
print(dq)  #deque([1,2,3])
