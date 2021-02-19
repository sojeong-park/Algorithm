# 커리큘럼 303p
# 듣고자 하는 강의수 N개가 주어지고
# 그 다음줄 부터는 각 강의의 시간과 그 강의를 듣기위해 먼저 들어야 하는 강의번호 주어짐. 각 줄은 -1로 끝남
# N개의 강의 수강하기까지 걸리는 최소 시간 한줄에 하나씩 출력력
# 출력예시 10 20 14 18 17
# 입력예시
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

from _collections import deque
import copy

n = int(input())
indegree = [0] * (n+1) # 진입차수
graph = [[]for i in range(n+1)] # 그래프 연결 정보
time = [0] * (n+1) # 가중치

# 방향 그래프 모든 간선 정보 입력받기
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology():
    result = copy.deepcopy(time)
    q = deque()
    # 진입차수가 0인 초기값 세팅
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for j in graph[now]:
            result[j] = max(result[j], result[now]+time[j])
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    for i in range(1, n+1):
        print(result[i])

topology()




