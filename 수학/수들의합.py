# https://www.acmicpc.net/problem/1789

def solution():
    n = int(input())
    sum, count, i = 0, 0, 1
    while True:
        if sum > n:
            break
        sum += i
        i += 1
        count += 1
    print(count-1)

solution()