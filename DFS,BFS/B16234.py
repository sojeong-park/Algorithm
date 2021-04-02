# 인구이동 https://www.acmicpc.net/problem/16234
from _collections import deque

n, L, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    united[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <=ny < n and united[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    united[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary
    return count

total_count = 0

