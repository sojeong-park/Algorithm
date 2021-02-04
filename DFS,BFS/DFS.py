# 깊이우선탐색 DFS 구현 - 재귀함수 구현

def dfs(gragh, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)

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
dfs(gragh, 1, visited)