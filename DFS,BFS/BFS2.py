def iterative_bfs(start_v):
    discovered = [start_v]
    que = [start_v]
    while que:
        v = que.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                que.append(w)
    return discovered

graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [4],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

print(iterative_bfs(1))