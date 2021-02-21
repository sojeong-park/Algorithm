# 백준 - 뒤집기 ( 1439 )
# https://www.acmicpc.net/problem/1439

n = list(input())

count = [0] * 2
for i in range(1, len(n)):
    if n[i-1] != n[i]:
        index = int(n[i-1])
        count[index] += 1

index = int(n[len(n)-1])
count[index] += 1
print(min(count[0], count[1]))