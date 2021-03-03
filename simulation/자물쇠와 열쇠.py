# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotateMatrix90(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(newLock):
    lockLength = len(newLock) // 3
    for i in range(lockLength, lockLength * 2):
        for j in range(lockLength, lockLength * 2):
            if newLock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    lockLen = len(lock)
    keyLen = len(key)

    newLock = [[0] * (lockLen*3) for _ in range(lockLen * 3)] # 자물쇠의 3배 크기 배열 만들기
    for i in range(lockLen): # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
        for j in range(lockLen):
            newLock[i + lockLen][j + lockLen] = lock[i][j]

    for r in range(4): # 4가지 방향에 대해서 확인
        key = rotateMatrix90(key) # 열쇠 90도 회전
        for x in range(lockLen * 2):
            for y in range(lockLen * 2):
                for i in range(keyLen): #자물쇠에 열쇠를 끼워 넣기
                    for j in range(keyLen):
                        newLock[x+i][y+j] += key[i][j]
                if check(newLock) == True: # 새로운 자물쇠에 열쇠가 정확히 맞는지 체크
                    return True
                for i in range(keyLen): # 자물쇠에서 열쇠 다시 빼기
                    for j in range(keyLen):
                        newLock[x+i][y+j] -= key[i][j]
    return False
