# https://www.acmicpc.net/problem/14502
# dfs 풀이 시간초과 발생

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = []
temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤의 인덱스


for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2 # 해당 위치에 바이러스 배치하고 다시 재귀 실행
                virus(x, y)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색을 이용해 울타리 설치하면서 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    #울타리가 3개 설치된 경
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n): # 각 바이러스 위치에서 전파 진
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)