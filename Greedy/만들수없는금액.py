# N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값을 구해라
# N=5, 주어진 동전이 3원,2원,1원,1원,9원일때 만들수 없는 양의 정수 금액 중 최솟값은 8원이다.

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

target = 1
for x in arr:
    if target < x:
        break
    target += x

print(target)