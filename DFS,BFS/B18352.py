# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기

from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if result[i] == -1:
                result[i] = result[v] + 1
                queue.append(i)


n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = [-1] * (n+1)
result[x] = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

bfs(graph, x)
check = False

for i in range(1, len(result)):
    if result[i] == k:
        print(i, end="\n")
        check = True

if check == False:
    print(-1)



