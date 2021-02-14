# 미래도시 259p
# 플로이드 워셜 알고리즘 풀이

INF = int(1e9)

n,m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 값은 0 입력
for i in range(1, n+1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 무방향 그래프
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split()) # k를 거쳐 x로 가는 최소 이동 시간 구하기

for i in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

