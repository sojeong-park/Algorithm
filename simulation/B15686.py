# https://www.acmicpc.net/problem/15686
# 치킨 배달
from itertools import combinations

n, m = map(int, input().split())

home = []
chicken = []

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            home.append((i, j))
        elif arr[j] == 2:
            chicken.append((i, j))


# 모든 치킨집 중 m 개의 치킨집 뽑는 조합
candidates = list(combinations(chicken, m))

print(candidates)

def get_sum(candidates):
    result = 0
    for h1, h2 in home:
        minValue = 1e9
        for c1, c2 in candidates:
            minValue = min(minValue, abs(h1-c1) + abs(h2 - c2))
        result += minValue
    return result

result = 1e9
for candidates in candidates:
    result = min(result, get_sum(candidates))

print(result)