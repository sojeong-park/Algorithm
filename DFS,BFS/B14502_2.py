# https://www.acmicpc.net/problem/14502
# combination 함수 활용, bfs로 변경
from itertools import combinations
from _collections import deque
import copy

n, m = map(int, input().split())
data = []
zero = [] # 빈칸의 좌표
temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤의 인덱스
tmpWalls = [] # 조합으로 골라낸 벽의 좌표들

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if data[i][j] == 0:
            zero.append((i, j))

tmpWalls = list(combinations(zero, 3))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(tmp):
    que = deque()
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                que.append((i,j))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if tmp[nx][ny] == 0:
                    que.append((nx, ny))
                    tmp[nx][ny] = 2



def get_score(tmpData):
    score = 0
    for i in range(n):
        for j in range(m):
            if tmpData[i][j] == 0:
                score += 1
    return score

for i in tmpWalls:
    tmpData = copy.deepcopy(data) # 맵 초기화
    for a, b in i:
        tmpData[a][b] = 1
    virus(tmpData)
    result = max(result, get_score(tmpData))

print(result)