# 기본적인 서로소 집합 알고리즘

# 경로 압축 기법 개선
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

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v + 1):
    parent[i] = i

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    unionParent(parent, a, b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1, v+1):
    print(findParent(parent, i), end = ' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블:', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')