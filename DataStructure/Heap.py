import heapq
'''heapq는 별도의 자료구조가 아닌 리스트를 인자로 사용한다.
즉, 리스트를 이용한 힙연산 모듈 이라고 생각하면 된다.
따라서 리스트로 가능한 연산까지 모두 사용할 수 있다.
(원소의 개수를 구하거나... 특정 위치의 원소 조회 등등)
'''
#최소 힙 생성
heap=[]

#힙에 원소 추가 O(logN)
heapq.heappush(heap,3)
heapq.heappush(heap,5)
heapq.heappush(heap,2)
heapq.heappush(heap,7)
#heap = [2,5,3,7]

#힙에서 원소 삭제 및 반환 O(logN), 비어 있는 경우 IndexError가 호출됨.
print(heapq.heappop(heap))
#heap = [3,5,7]

#여러개의 원소로 바로 힙 초기화 O(N)
heap=[3, 2, 4, 7, 5, 8, 1]
heapq.heapify(heap)
#heap=[1, 2, 3, 7, 5, 8, 4]

'''
파이썬 heapq 모듈은 최대힙이 구현되어 있지 않다. 따라서 최소힙으로 최대힙을 구현해야한다.
이는 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로
최소 힙이 구성되는 원리를 이용한다. maxheap.heappush((우선순위, 값))
'''
#최대 힙 생성
heap_items = [3,5,2,7]
maxHeap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

#최대 힙 삽입
maxHeap=[]
heapq.heappush(maxHeap,(-3,3))
heapq.heappush(maxHeap,(-5,5))
heapq.heappush(maxHeap,(-2,2))
heapq.heappush(maxHeap,(-7,7))
#maxHeap=[(-7, 7), (-5, 5), (-2, 2), (-3, 3)]

#최대 힙 삭제 및 반환 (우선순위에 관심없으므로 [1]로 값만 반환함
print(heapq.heappop(maxHeap)[1])

'''
응용1. K번째 최소값/최대값
배열을 최소힙/최대힙으로 만든 후, heappop()을 K번 호출하면 K번째 최소값/최대값을 구할 수 있다.
'''
def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min
'''
응용2. 힙 정렬
K번째 최소값/최대값 구하는 것과 마찬가지로, heap에 해당하느 리스트의 크기가 0이 될 때까지
heappop()을  호출하고 저장하면 정렬된 리스트가 나온다.
'''
def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

'''출처:https://www.daleseo.com/python-heapq'''
