# 플로이드-워셜 알고리즘 구현
# 현재 노드를 거쳐가는 모든 경로 고려 즉, 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보 저장

INF = int(1e9)

n = int(input()) # 노드 수
m = int(input()) # 간선 수

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에게 가는 비용 0 으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선의 가중치값 입력
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()