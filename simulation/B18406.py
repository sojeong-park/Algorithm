# https://www.acmicpc.net/problem/18406

import sys

input = sys.stdin.readline

n = input()

size = (len(n)//2) - 1

sum1 = 0
for i in range(0, size+1):
    sum1 += int(n[i])

sum2 = 0
for i in range(size+1, len(n)-1):
    sum2 += int(n[i])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')