# https://www.acmicpc.net/problem/15650

import sys
n, m = map(int, input().split())
c = [False]*(n+1)
a = [0] * m

result = 0
def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(start, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, i+1, n, m)
        c[i] = False

go(0,1,n, m)