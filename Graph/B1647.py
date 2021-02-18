# 백준 1647 도시 분할 계획
# https://www.acmicpc.net/problem/1647

import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i # 부모노드 저장전 자기 자신으로 초기화.

edges = [] # 모든 간선의 정보 담을 리스트

for i in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

totalCost = 0
lastCost = 0
edges.sort()
for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        totalCost += cost
        lastCost = cost
print(totalCost - lastCost)


