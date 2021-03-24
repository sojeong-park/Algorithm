# N개의 수로 된 수열 a[1]~a[n]이있다.
# 이 수열의 i번째 수부터 j번째 수까지의 합 a[i]+a[i+1]+---+a[j-1]+a[j] 가 m이 되는 경우의 수를 구해라

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
# 적은수일경우 정상동작하나 100000일경우 시간초과발생
# for k in range(n+1):
#     i = 0
#     j = k
#     while j < n:
#         if sum(a[i:j+1]) == m:
#             ans += 1
#         i += 1
#         j += 1

lt = 0
rt = 1
total = a[lt]

while True:
    if total < m:
        if rt < n:
            total += a[rt]
            rt += 1
        else:
            break
    elif total == m:
        total -= a[lt]
        lt += 1
        ans += 1
    else:
        total -= a[lt]
        lt += 1
print(ans)
