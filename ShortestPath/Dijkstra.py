# 다익스트라 알고리즘
# 간단한 다익스트라 알고리즘 구현

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input())
graph = [[] for i in range(n+1)] # 노드와 간선정보 담고있는 그래프
visited = [False] * (n + 1) # 방문체크 리스트
distance = [INF] * (n + 1) # 최단거리 입력 테이블을 모두 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a -> b 로가는 비용의 값이 c

# 가장 짧은 거리 노드 번호 반환
def getSmallNode():
    minValue = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n - 1):
        now = getSmallNode()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])