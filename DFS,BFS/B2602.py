# 백준 2606 바이러스
# 문제설명 https://www.acmicpc.net/problem/2606

from _collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input()) # 컴퓨터 개수
m = int(input()) # 간선 수

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 연결 컴퓨터 번호 입력 받기
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(n):
    que = deque([n])
    visited[n] = True
    result = 0
    while que:
        x = que.popleft()
        for i in graph[x]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True
                result += 1
    return result
print(bfs(1))