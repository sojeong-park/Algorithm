# 인구이동 https://www.acmicpc.net/problem/16234
from _collections import deque

def bfs(gragh, start, visited):
    que = deque([start])
    visited[start] = True
    # que가 null일때까지 반복
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in gragh[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

n, L, m = map(int, input().split())

a = []
visit = [[0]*n for _ in range(n)]

for i in range(n):
    a.append(list(map(int, input().split())))
