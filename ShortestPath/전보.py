# 전보 - 282p간
# x 도시와 연결된 여러 도시에 모든 메시지를 보내는 총 시간과 도시 개수를 구하기
# 입력
# 3 2 1 -> 도시개수, 통로개수, 메시지 보내고자 하는 도시
# 1 2 4 -> 1번 노드에서 2번 노드로 메시지 통로가 존재하며 4만큼의 시간이 소요된다
# 1 3 2
# 출력
# 2 4 -> 메시지 받는 총 도시개수, 메시지 전송에 걸리는 총 시간
import heapq
INF = int(1e9)
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]  * (n+1)

for _ in range(m):
    a,b,x = map(int, input().split())
    graph[a].append((b,x))

# 시작점에서 도달할수 있는 모든 도시를 구하는 문제이므로 한 도시에서 다른 도시까지의 최단거리 문제로 치환 가능
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
maxDistance = 0

for d in distance:
    if d != INF:
        count += 1
        maxDistance = max(maxDistance, d)

print(count - 1, maxDistance)
