# https://programmers.co.kr/learn/courses/30/lessons/60061

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
def solution(n, build_frame):
    arr = [[2]*(n+1) for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if a == 0: # 기둥
            if b == 0: # 삭제
                if arr[x-1][y+1]==1 and arr[x+1][y+1]==1:
                    arr[x][y] = 2
                elif arr[x+1][y] == 0:
                    arr[x][y] = 2
            else: # 설치
                if y==0 or arr[x-1][y]==1 or arr[x][y-1] == 0:
                    arr[x][y] = 0
        else: # 보
            if b == 0: # 삭제
                if arr[x][y-1] == 0:
                    arr[x][y] = 2
            else: # 설치
                if arr[x-1][y] == 1 and arr[x+1][y] == 1:
                    arr[x][y] = 1
                elif arr[x][y-1] == 0 or arr[x+1][y-1] == 0:
                    arr[x][y] =1
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] != 2:
                answer.append([i,j,arr[i][j]])
    return answer

print(solution(n, build_frame))