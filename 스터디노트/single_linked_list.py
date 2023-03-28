# 2차원의 데이터를 사용하는 단순 연결 리스트를 완성하라.
# 출력 예시
## 초기 연결 리스트 ##
# [1, '파이썬'] [2, 'C'], [3, 'C++'], [4, 'JAVA'], [5, 'MATLAB'], 
# ## R 삽입 결과 ##
# [0, 'R'] [1, '파이썬'], [2, 'C'], [3, 'C++'], [4, 'JAVA'], [5, 'MATLAB'], 
# ## JAVA 삭제 결과 ##
# [0, 'R'] [1, '파이썬'], [2, 'C'], [3, 'C++'], [5, 'MATLAB'], 
# ## MATLAB 검색 결과 ##
# [5, 'MATLAB']

class Node():
    def __init__ (self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ', ')

def insertNode(findData, insertData):
    global memory, head, current, pre
    # 코드 작성 부분
    if head.data[1] == findData:
      node = Node()
      node.data = insertData
      node.link = head
      head = node
    else:
      current = head
      find_flag = False
      while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
          node = Node()
          node.data = insertData
          node.link = current
          pre.link = node
          find_flag = True
          break
      if not find_flag:
        node = Node()
        node.data = insertData
        current.link = node



def deleteNode(deleteData):
    global memory, head, current, pre

    # 코드 작성 부분
    if head.data[1] == deleteData:
      current = head
      head = head.link
      del current
    else:
      current = head
      # 다음 노드가 없을 때까지 반복하겠다
      while current.link != None:
        pre = current
        # 다음 노드를 가르키겠다
        current = current.link
        if current.data[1] == deleteData:
          pre.link = current.link
          del current
          break

def findNode(findData):
    global memory, head, current, pre
    current = head

    # 코드 작성 부분
    if current.data[1] == findData:
      result = current
    else:
      find_flag = False
      while current.link != None:
        current = current.link
        if current.data[1] == findData:
          result = current
          find_flag = True
          break

      if not find_flag:
        result = Node()

    return result

# 실행 구문
memory = []
head, current, pre = None, None, None
dataArray = [ [1, '파이썬'], [2, 'C'], [3, 'C++'], [4, 'JAVA'], [5, 'MATLAB'] ]  # 2차원 데이터

node = Node()			# 첫 번째 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :		# 두 번째 노드부터
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

print('## 초기 연결 리스트 ##')
printNodes(head)

print('\n## R 삽입 결과 ##')
insertNode('파이썬', [0, 'R'])
printNodes(head)

print('\n## JAVA 삭제 결과 ##')
deleteNode('JAVA')
printNodes(head)

print('\n## MATLAB 검색 결과 ##')
f_node = findNode('MATLAB')
print(f_node.data)