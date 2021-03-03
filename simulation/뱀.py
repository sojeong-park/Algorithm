# https://www.acmicpc.net/problem/3190
#  왼쪽('L')오른쪽('D') 90도 회전

n = int(input())
m = int(input())
arr = [[0]*(n+1) for _ in range(n+1)] # 맵 정보

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1

k = int(input())
directions = [] # z 초일때 방향 전환한다. 방향 정보

for _ in range(k):
    z, direction = input().split()
    directions.append((int(z),direction))

#d = [(-1,0), (0,1),(1,0),(0,-1)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def directionChange(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction

def solution():
    count, x, y = 0, 1,1
    arr[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 초기 오른쪽 방향
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and arr[nx][ny] != 2: # 맵의 범위안에 존재하고 뱀의 몸통이 없는 위치인경우
            if arr[nx][ny] == 0: #사과가 없을 경우 꼬리 제거
                arr[nx][ny] = 2 # 뱀의 몸통위치
                q.append([nx, ny])
                px, py = q.pop(0)
                arr[px][py] = 0
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append([nx,ny])
        else:
            count += 1
            break
        x, y = nx, ny
        count += 1
        if index < 1 and count == directions[index][0]:
            direction = directionChange(direction, directions[index][1])
            index += 1
    return count

print(solution())
