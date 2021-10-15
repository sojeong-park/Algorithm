# https://www.acmicpc.net/problem/16953
from collections import deque

def solution(n, m):
    res = -1
    que = deque([(n, 1)])
    while que:
        i, cnt = que.popleft()
        if i == m:
            res = cnt
            break;
        if i*2 <= m:
            que.append((i*2, cnt+1))
        if int(str(i)+'1') <= m:
            que.append((int(str(i)+'1'), cnt + 1))
    return res

n, m = map(int, input().split())
print(solution(n, m))