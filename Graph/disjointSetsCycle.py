# 서로소 집합을 활용한 사이클 판별
# 무방향 그래프에서만 판별 가능

# 특정 원소가 속한 집합 찾기
def findUnion(parent, x):
    # 루트노드가 아니라면, 루트노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = findUnion(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def unionParent(parent, a, b):
    a = findUnion(parent, a)
    b = findUnion(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if findUnion(parent, a) == findUnion(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않은 경우 합집합 수행
    else:
        unionParent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 발생하지 않음')