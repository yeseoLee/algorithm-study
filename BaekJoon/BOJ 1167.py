import sys
input = sys.stdin.readline

# input & init
n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n):
    li = list(map(int, input().split()))
    v1 = li[0]
    for i in range(1, len(li) - 1, 2):
        v2, d = li[i], li[i + 1]
        graph[v1].append((v2, d))

max_d = 0
far_node = 0


# logic
def dfs(now_v, now_d):
    global max_d
    global far_node
    if max_d < now_d:
        max_d = now_d
        far_node = now_v

    visited[now_v] = True
    for next_v, next_d in graph[now_v]:
        if not visited[next_v]:
            dfs(next_v, next_d + now_d)


visited = [False for _ in range(n + 1)]
dfs(1, 0)
visited = [False for _ in range(n + 1)]
dfs(far_node, 0)

print(max_d)

"""
문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 
트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)
둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 
하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 
정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 
각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
예제 출력
11 (2->4->3->1) (4+5+2)
11 (1->3->4->5) (2+3+6)
"""

# solution : https://blog.myungwoo.kr/112