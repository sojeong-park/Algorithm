# https://www.acmicpc.net/problem/3085
# max 함수 사용시 시간초과 발생
import sys
input=sys.stdin.readline

def solution():
    n=int(input())
    arr = [list(input()) for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n-1):
            # 좌우
            arr[i][j], arr[i][j + 1] = arr[i][j+1], arr[i][j]
            temp = check(arr)

            if temp > answer:
                answer = temp
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            # 상하
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            temp = check(arr)

            if temp > answer:
                answer = temp
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
    print(answer)

def check(s):
    answer = 0
    for i in range(len(s)):
        #열 순회
        cnt = 1
        for j in range(1, len(s)):
            if s[i][j] == s[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if answer < cnt:
                answer = cnt
        #행 순회
        cnt = 1
        for j in range(1, len(s)):
            if s[j][i] == s[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if answer < cnt:
                answer = cnt
    return answer

solution()

