# 위상정렬
# 입력
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

from _collections import deque
v, e = map(int, input().split())

indegree = [0] * (v+1) # 모든 노드에 대한 진입차수 0으로 초기화
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
def topology():
    q = deque()
    # 진입차수가 0인 값 insert
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1 # 진입차수 제거
            if indegree[i] == 0: # 진입차수가 0이면 큐에 추가
                q.append(i)

topology()
# 위상 정렬 수행 결과 출력
for i in result:
    print(i, end=' ')