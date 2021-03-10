# https://www.acmicpc.net/problem/18405

from _collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
que = deque(data)

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
while que:
    virus, time, ax, ay = que.popleft()
    if time == s:
        break
    for i in range(4):
        nx = ax + dx[i]
        ny = ay + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:  # 배열
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                que.append((virus, time+1, nx, ny))

print(graph[x-1][y-1])
