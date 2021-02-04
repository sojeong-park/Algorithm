# 너비우선탐색 BFS 구현 - deque 라이브러리 사용

from _collections import deque

def bfs(gragh, start, visited):
    que = deque([start])
    visited[start] = True
    # que가 null일때까지 반복
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in gragh[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

gragh = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
        ]
visited = [False] * 9
bfs(gragh, 1, visited)