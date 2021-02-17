# 크루스칼 알고리즘
# 입력        결과 159
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

# 모든 간선을 담을 리스트
edges =[]
# 최종 비용
result = 0

for i in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost

print(result)