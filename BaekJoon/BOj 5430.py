import sys
from collections import deque

t=int(sys.stdin.readline())
for i in range(t):
    # 실행할 함수p (R 또는 D)
    cmd=sys.stdin.readline().rstrip()
    #배열 원소 개수(배열의 길이)
    n=int(sys.stdin.readline()) 
    #배열에 들어있는 수
    dq=sys.stdin.readline()
    #덱
    if(n==0): dq=deque()
    else: dq=deque(list(map(int,dq[1:-2].split(','))))
    #배열이 뒤집어져있는지
    isReverse=False
    left,right=0,0
    for p in cmd:
        if(p=='R'):
            isReverse=(not isReverse)
        else : #p=='D'
            if dq:
                if(not isReverse):
                    dq.popleft()
                else:
                    dq.pop()
            else:
                print('error')
                break        
    else:
        if(isReverse):
            dq=reversed(dq)
        print("[" + ",".join(list(map(str,dq))) + "]")

'''
1. 처음에는 반복문 내에서 입력받는 모든 함수에 대해 동작하도록 작성하였으나
시간 초과가 발생해서 뒤집기는 일종의 flag를 이용하여 실제로 배열은 그대로 있고
flag 값에 따라 앞에서 버리거나, 뒤에서 버리도록 해서 해결.

2.자꾸 list(dq)로 출력하느라 시간낭비했다.
출력 형태를 잘 보자. 띄어쓰기 없이 [1,2,3,4,5]로 되어있기 때문에
문자열 리스트로 바꾸고, .join을 이용해서 출력형태를 맞춤.
'''
