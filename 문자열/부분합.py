# https://www.acmicpc.net/problem/1806
import sys

n, m = map(int, input().split())
num = list(map(int, input().split()))

left, right, tmp_sum = 0, 0, 0
min_length = sys.maxsize

# 투포인터
while True:
    if tmp_sum >= m:
        min_length = min(min_length, right-left)
        tmp_sum -= num[left]
        left += 1
    elif right == n:
        break
    else:
        tmp_sum += num[right]
        right += 1

if min_length == sys.maxsize:
   print(0)
else:
   print(min_length)
