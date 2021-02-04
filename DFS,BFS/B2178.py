# 백준 2178 미로탐색 - bfs풀이 (시작지점에서 가까운 노드부터 차례로 탐색하기에 bfs가 적합)
# 0: 방문 불가 1: 방문가능, 상하좌우로 탐색

from _collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    que = deque([])
    que.append((x,y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            kx = x+dx[i]
            ky = y+dy[i]
            if kx >= 0 and kx < n and ky >= 0 and ky < m:
                if graph[kx][ky] == 1:
                    que.append([kx, ky])
                    graph[kx][ky] += graph[x][y]

bfs(0,0)

print(graph[n-1][m-1])
