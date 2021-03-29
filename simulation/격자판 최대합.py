# 각 행, 열, 두 대각선의 합 중 가장 큰 수를 구하는 프로그램을 작성하시오

n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

res1 = 0
res2 = 0
largest = 0
for i in range(n):
    for j in range(n):
        res1 += a[i][j] # 각 열의
        res2 += a[j][i] # 각 행의 합합
    if res1 > res2:
        largest = res1
    else:
        largest = res2
    res1, res2 = 0, 0


for i in range(n):
    res1 += a[i][i]
    res2 += a[i][n-i-1]

largest = max(res1, res2, largest)

print(largest)