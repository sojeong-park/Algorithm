# https://www.acmicpc.net/problem/14888
# 수열만들기 예시
# pool = ['A', 'B', 'C']
# print(list(map(''.join, permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, permutations(pool, 2)))) # 2개의 원소로 수열 만들기

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxValue = -1e9
minValue = 1e9

def dfs(i, now):
    global minValue, maxValue, add, sub, mul, div
    if i == n:
        minValue = min(minValue, now)
        maxValue = max(maxValue, now)
    else:
        if add>0:
            add -= 1
            dfs(i+1, now+nums[i])
            add += 1
        if sub>0:
            sub -= 1
            dfs(i+1, now-nums[i])
            sub += 1
        if mul>0:
            mul -= 1
            dfs(i+1, now * nums[i])
            mul += 1
        if div>0:
            div -= 1
            dfs(i+1, int(now / nums[i]))
            div += 1

dfs(1, nums[0])
print(maxValue)
print(minValue)