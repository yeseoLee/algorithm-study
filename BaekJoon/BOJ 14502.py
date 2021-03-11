n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
print(arr)

'''
바이러스 탐색
모든 바이러스 격리 가능한지
가능하면 가장 넒은 영역을 남기고 출력
불가능하면 벽을 이용해 가장 큰 안전 영역을 만들어 출력
