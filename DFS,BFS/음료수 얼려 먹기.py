# 0->빈칸,  1->칸막이 빈칸에 음료수를 부어 몇개의 아이스크림을 만들수 있을까
# 입력, 정답은 3
# 4 5
# 00110
# 00011
# 11111
# 00000

# 상하좌우 탐색위한 좌표 변수
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1
print(count)